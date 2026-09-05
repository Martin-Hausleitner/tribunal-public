// Public pack API registration only. No Squinch renderer or generated-output patch.
import fs from 'node:fs';
import path from 'node:path';
import {pathToFileURL} from 'node:url';
const modules = process.env.SQUINCH_NODE_MODULES;
const root = process.env.SQUINCH_ATLAS_PACK;
if (!modules || !root) throw new Error('Set approved SQUINCH_NODE_MODULES and SQUINCH_ATLAS_PACK paths');
const pack = path.resolve(root);
const {registerPack} = await import(pathToFileURL(path.join(path.resolve(modules), '@squinch/core/dist/index.js')).href);
const manifest = JSON.parse(fs.readFileSync(path.join(pack, 'pack.json'), 'utf8'));
if (manifest.name !== 'atlas' || manifest.monochrome !== true) throw new Error('Unexpected atlas pack contract');
registerPack(manifest, (file) => {
  if (!/^[a-z0-9-]+\.svg$/.test(file)) throw new Error('Unsafe native pack asset');
  const filename = fs.realpathSync(path.join(pack, 'icons', file));
  const relative = path.relative(fs.realpathSync(pack), filename);
  if (relative.startsWith('..') || path.isAbsolute(relative)) throw new Error('Pack asset escapes root');
  return fs.readFileSync(filename, 'utf8');
});
