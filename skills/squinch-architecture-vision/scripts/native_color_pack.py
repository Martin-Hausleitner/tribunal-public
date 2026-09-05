#!/usr/bin/env python3
"""Copy pinned generic SVG artwork unchanged; add native pack colour metadata."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil

PALETTE = {'red':'#B5544C','amber':'#A06B12','green':'#3F8A5C','teal':'#1F8A80','blue':'#3A6EA8','violet':'#6B5FC9','pink':'#B04A8A','gray':'#7A776E','accent':'#5A57C9'}


def prepare(model_path: Path, sys_pack: Path, output: Path) -> int:
    model = json.loads(model_path.read_text(encoding='utf-8'))
    upstream = json.loads((sys_pack / 'pack.json').read_text(encoding='utf-8'))
    if model_path.stat().st_size > 8_000_000:
        raise ValueError('Model exceeds the 8 MB source budget')
    icons, proof, assets, updates = {}, {}, {}, []
    for node in model['nodes']:
        original = node.get('icon_original', node['icon'])
        if not original.startswith('sys/'):
            continue
        name, hue = original.split('/', 1)[1], node['color']
        if name not in upstream['icons'] or hue not in PALETTE or not re.fullmatch(r'[a-z0-9-]+', name):
            raise ValueError('Unknown native icon or hue')
        filename = upstream['icons'][name]['file']
        if not re.fullmatch(r'[a-z0-9-]+\.svg', filename):
            raise ValueError('Unsafe upstream asset path')
        source = (sys_pack / 'icons' / filename).resolve()
        if not source.is_relative_to(sys_pack.resolve()):
            raise ValueError('Upstream asset escapes pack')
        data = source.read_bytes()
        ident = name + '-' + hue
        icons[ident] = {'file':name+'.svg','title':upstream['icons'][name]['title']+' / '+hue,'category':'Atlas semantics','color':PALETTE[hue]}
        proof[ident] = {'id':ident,'source':original,'sha256':hashlib.sha256(data).hexdigest(),'artwork_modified':False}
        assets[name+'.svg'] = data
        updates.append((node, original, ident))
    output.mkdir(parents=True, exist_ok=True)
    (output / 'icons').mkdir(exist_ok=True)
    for filename, data in assets.items():
        destination = output / 'icons' / filename
        if not destination.resolve().is_relative_to(output.resolve()) or destination.is_symlink():
            raise ValueError('Output asset escapes pack')
        destination.write_bytes(data)
    for filename in ('LICENSE', 'NOTICE'):
        if (sys_pack / filename).is_file():
            shutil.copyfile(sys_pack / filename, output / filename)
    manifest = {'name':'atlas','title':'Atlas semantic color plates','release':'1.0.0','source':'https://lucide.dev','license':'ISC','attribution':'Lucide via pinned @squinch/pack-sys; unchanged artwork with native colour metadata. Not vendor logos.','monochrome':True,'icons':icons}
    (output / 'pack.json').write_text(json.dumps(manifest, indent=2)+'\n', encoding='utf-8')
    (output / 'asset-proof.json').write_text(json.dumps({'source_release':upstream.get('release'),'icons':list(proof.values()),'renderer_modified':False}, indent=2)+'\n', encoding='utf-8')
    for node, original, ident in updates:
        node['icon_original'], node['icon'] = original, 'atlas/'+ident
    packs = model.setdefault('packs', [])
    if not any(p.get('name') == 'atlas' for p in packs):
        packs.append({'name':'atlas','from':'./icons/atlas'})
    model_path.write_text(json.dumps(model, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    return len(icons)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('model', type=Path)
    parser.add_argument('sys_pack', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    try:
        print(prepare(args.model, args.sys_pack, args.output))
    except (OSError, ValueError, KeyError, TypeError) as error:
        parser.exit(2, f'BLOCKED: {error}\n')
