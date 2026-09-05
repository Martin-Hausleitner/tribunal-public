#!/usr/bin/env python3
from pathlib import Path
import argparse

# Deterministic semantic blueprint for the public reference mega diagram.
# It is intentionally generic: private source evidence remains in the hosts.
SYSTEMS = [
("entry","Agent Entry & Heartbeat","blue","sys/log-in",[
("Bootstrap","blue",["AGENTS.md","HEARTBEAT.md","Pinned Skill"]),("Discovery","teal",["Hans Queue Scan","GitHub Issue Scan","Scope Resolver"]),("Claim & Resume","violet",["Claim Acquire","Lease / Fence","Resume Existing Work"]),("Entry Policy","red",["Trust Check","Authority Boundary","Durable Handoff"])]),
("hans","Hans","green","sys/brain",[
("Durable Work","green",["Inbox","Hans Queue","Receipts"]),("Knowledge Core","teal",["Canonical Homes","Views & Graph","Sources"]),("Git Federation","blue",["Git Submodules","Coverage Ledgers","Versioned History"]),("Tribunal Host","pink",["skill: tribunal","Private Ledger Ref","docs/tribunal/changes"])]),
("agent","Agent-Concept","violet","sys/bot",[
("Context Routing","violet",["Agent-Concept Router","Skill Resolver","Contract Router"]),("Runtime & Orchestration","blue",["Orchestrator","Session Management","Tool Bus"]),("Context Fabric","teal",["Selective Loader","Hans Connector","Provenance Router"]),("Primary Surface","pink",["React-first UI","Browser Shell","Native Capability Bridge"])]),
("oam","Omni Audio Matrix","amber","sys/audio-waveform",[
("Capture","amber",["Microphone Capture","System Audio","File / Device Upload"]),("Speech Pipeline","blue",["VAD","ASR Ensemble","Diarization"]),("Speaker & Context","green",["Speaker ID","ContextSpan","Canonical Revision"]),("Outputs","teal",["Compression / Summary","Review UI","Matrix Projection"])]),
("tribunal","Tribunal","pink","sys/scale",[
("Review Intake","pink",["Review Request","Review Claim","Evidence Packet"]),("Independent Reviewers","violet",["Facts / Correctness","Risk / Security","Scope / Fidelity"]),("Deterministic Gate","red",["GO","CONDITIONAL_GO","NO_GO / NEEDS_*"]),("Fresh Fix Loop","amber",["Condition IDs","New Target Commit","Fresh Re-Review"])]),
("openspec","OpenSpec & Workflows","teal","sys/file-stack",[
("Discovery","teal",["Problem / Goal","Research Inputs","Architecture Decision"]),("Specification","blue",["Proposal","Design","Specs"]),("Delivery","green",["Tasks","Implementation","Verification"]),("Rollout","amber",["Conditional Tasks","Release Gate","Archive / Receipt"])]),
("skills","Skills & Public Modules","green","sys/puzzle",[
("Skill Discovery","green",["Metadata Router","SKILL.md","On-demand Resources"]),("Public Skills","blue",["Tribunal Skill","Squinch DSL Skill","Quality Skills"]),("Private Hosts","violet",["Hans Mount","Agent-Concept Mount","Company Hosts"]),("Skill Evals","amber",["Trigger Evals","Contract Tests","Drift Checks"])]),
("browser","Browser & React UI","blue","sys/monitor-up",[
("Browser Shell","blue",["Workspaces / Tabs","Browser Automation","Screenshot Capture"]),("Architecture Viewer","violet",["Self-contained HTML","Squinch Views","Presentation Mode"]),("Visual Review","pink",["Desktop QA","Responsive QA","Vision Inspection"]),("Product UI","teal",["Dashboard","Waveform / Timeline","Search / Graph"])]),
("matrix","Matrix","violet","sys/messages-square",[
("Rooms & Threads","violet",["Spaces","Threads","Sender Identity"]),("Event Projection","blue",["Status Events","Tribunal Events","Audio Events"]),("Human Loop","pink",["Review Interaction","Corrections","Handoff"]),("Audit Projection","gray",["Canonical Links","Event History","Privacy Filter"])]),
("gitfabric","Git Fabric & CI","blue","sys/git-branch",[
("Repository Layer","blue",["Main / Protected","Branches / PRs","Gitlinks"]),("Worktrees","violet",["Isolated Worktree","Claim Mapping","Conflict Resolution"]),("Continuous Verification","green",["Unit / Contract","E2E / Failure Injection","Evidence Artifacts"]),("Release Discipline","amber",["Required Checks","Merge Gate","Main Readback"])]),
("evidence","Evidence & Provenance","pink","sys/fingerprint",[
("Source Evidence","pink",["Primary Sources","Repository Evidence","Research Corpus"]),("Executable Evidence","green",["Command Output","Benchmark","Failure Injection"]),("Visual Evidence","blue",["Screenshots","Visual Compare","Vision QA Notes"]),("Receipt Chain","gray",["Evidence SHA-256","Receipt","Retention / Privacy"])]),
("execution","Execution & Agent Fleet","amber","sys/workflow",[
("Agent Fleet","amber",["Manager","Workers","Reviewers"]),("Orchestration","violet",["Dependency DAG","Budget / Capacity","Pause / Resume"]),("Tool Execution","blue",["CLI / Shell","MCP Tools","Browser / CU"]),("Recovery","red",["Bounded Retry","Rollback","Human Escalation"])]),
("observability","Observability","teal","sys/chart-no-axes-combined",[
("Telemetry","teal",["Structured Events","Metrics","Traces"]),("Status Surfaces","blue",["Agent Status","Project Status","System Health"]),("Alerts","amber",["Blocker Alert","Drift Alert","Quality Regression"]),("Reports","gray",["Daily / Weekly","Tribunal Register","Proof Index"])]),
("security","Security & Authority","red","sys/shield",[
("Identity & Access","red",["Owner Scope","Agent Identity","Authorization"]),("Privacy","pink",["Data Minimization","Raw Evidence Private","Retention Policy"]),("Secrets","violet",["Opaque References","Secret Store","Secret Scan"]),("Effect Authority","amber",["Read-only Default","Explicit Write","No Auto-Merge"])]),
("integrations","Protocols & Integrations","green","sys/plug",[
("Agent Protocols","green",["MCP","A2A","CLI Contract"]),("Git Forges","blue",["GitHub","GitLab / Forgejo","Azure DevOps"]),("Enterprise Apps","violet",["Microsoft 365","Google Workspace","Notion"]),("Media & Devices","amber",["Spotify Bridge","Mobile Devices","Desktop Hosts"])]),
("lifecycle","Closed-Loop Lifecycle","accent","sys/repeat-2",[
("Research","accent",["Question / Goal","Source Discovery","Synthesis"]),("Build","blue",["Spec","Task","Implementation"]),("Verify","green",["Tests","Visual QA","Tribunal"]),("Learn & Recover","violet",["Receipt","Hans Promotion","Next Iteration"])]),
("company","Company Departments","amber","sys/building-2",[
("Leadership","amber",["Strategy","Portfolio","Governance"]),("Product & Design","pink",["Product Research","Design / UX","Requirements"]),("Engineering","blue",["Architecture","Software Delivery","Platform / DevOps"]),("Operations & GTM","green",["Operations / Support","Sales / Customer","Finance / Admin"])]),
("research","Research Intelligence","teal","sys/search-check",[
("Discovery","teal",["Web Research","Repository Research","Internal Corpus"]),("Analysis","violet",["Comparison Matrix","Benchmark","Adversarial Research"]),("Visual Validation","pink",["Render","Vision Inspect","Iterate"]),("Promotion","green",["Decision Record","Promote to Hans","Source Links"])]),
]

ICONS={"blue":"sys/network","green":"sys/check-check","violet":"sys/waypoints","amber":"sys/zap","pink":"sys/eye","teal":"sys/activity","red":"sys/shield-alert","gray":"sys/history","accent":"sys/sparkles"}

def ident(text:str)->str:
    s=''.join(ch.lower() if ch.isalnum() else '_' for ch in text)
    while '__' in s:s=s.replace('__','_')
    s=s.strip('_')
    if not s or s[0].isdigit():s='n_'+s
    return s

def emit(out:Path):
    L=["// Hans + Agent-Concept + OAM + Tribunal mega architecture","// HTML is canonical output. Screenshots are visual-QA evidence.","theme dark","",'person operator "Martin / Operator"','person user "User / Team"',""]
    for sid,label,color,icon,containers in SYSTEMS:
        L += [f'system {sid} "{label}" {{',f'  color: {color}',f'  icon: {icon}','  preview: auto']
        paths=[]
        for clabel,ccolor,nodes in containers:
            cid=ident(clabel)
            L += [f'  container {cid} "{clabel}" {{',f'    color: {ccolor}',f'    description: "{clabel} capabilities"']
            nids=[]
            for nlabel in nodes:
                nid=ident(nlabel); nids.append(nid)
                L += [f'    {nid} = {ICONS[ccolor]} "{nlabel}" {{',f'      color: {ccolor}',f'      description: "{nlabel}"','    }']
            L += [f'    {nids[0]} -> {nids[1]} "feeds" {{ color: {ccolor} }}',f'    {nids[1]} -> {nids[2]} "verifies" {{ color: {ccolor} }}','  }']
            paths.append((cid,nids))
        for a,b in zip(paths,paths[1:]):
            L += [f'  {a[0]}.{a[1][-1]} -> {b[0]}.{b[1][0]} "handoff" {{ color: {color} }}']
        L += ['}','']

    def p(system,container,node):return f"{system}.{ident(container)}.{ident(node)}"
    E=[
      ('operator',p('entry','Bootstrap','AGENTS.md'),'starts','accent'),(p('entry','Discovery','Hans Queue Scan'),p('hans','Durable Work','Hans Queue'),'reads','blue'),
      (p('entry','Discovery','Scope Resolver'),p('agent','Context Routing','Agent-Concept Router'),'routes','blue'),(p('hans','Tribunal Host','skill: tribunal'),p('tribunal','Review Intake','Review Request'),'loads','pink'),
      (p('hans','Knowledge Core','Canonical Homes'),p('agent','Context Fabric','Hans Connector'),'context','green'),(p('agent','Context Routing','Skill Resolver'),p('skills','Skill Discovery','SKILL.md'),'activates','violet'),
      (p('agent','Context Routing','Contract Router'),p('openspec','Specification','Specs'),'reads','violet'),(p('agent','Runtime & Orchestration','Orchestrator'),p('execution','Orchestration','Dependency DAG'),'delegates','blue'),
      (p('oam','Capture','Microphone Capture'),p('oam','Speech Pipeline','VAD'),'audio','amber'),(p('oam','Speech Pipeline','ASR Ensemble'),p('oam','Speaker & Context','Speaker ID'),'segments','blue'),
      (p('oam','Speaker & Context','ContextSpan'),p('hans','Knowledge Core','Sources'),'promotes','green'),(p('oam','Outputs','Matrix Projection'),p('matrix','Event Projection','Audio Events'),'projects','teal'),
      (p('tribunal','Review Intake','Evidence Packet'),p('evidence','Receipt Chain','Evidence SHA-256'),'binds','pink'),(p('evidence','Visual Evidence','Vision QA Notes'),p('tribunal','Independent Reviewers','Scope / Fidelity'),'supports','blue'),
      (p('tribunal','Deterministic Gate','CONDITIONAL_GO'),p('openspec','Rollout','Conditional Tasks'),'creates conditions','amber'),(p('openspec','Rollout','Conditional Tasks'),p('execution','Orchestration','Dependency DAG'),'schedules fix','amber'),
      (p('execution','Tool Execution','CLI / Shell'),p('evidence','Executable Evidence','Command Output'),'produces','blue'),(p('execution','Tool Execution','Browser / CU'),p('evidence','Visual Evidence','Screenshots'),'produces','blue'),
      (p('tribunal','Fresh Fix Loop','Fresh Re-Review'),p('tribunal','Deterministic Gate','GO'),'may close','green'),(p('tribunal','Deterministic Gate','GO'),p('gitfabric','Release Discipline','Merge Gate'),'separate merge gate','green'),
      (p('gitfabric','Release Discipline','Main Readback'),p('hans','Durable Work','Receipts'),'records','blue'),(p('skills','Public Skills','Squinch DSL Skill'),p('browser','Architecture Viewer','Self-contained HTML'),'renders','green'),
      (p('browser','Visual Review','Vision Inspection'),p('research','Visual Validation','Vision Inspect'),'feeds','pink'),(p('research','Visual Validation','Iterate'),p('skills','Public Skills','Squinch DSL Skill'),'improves DSL','pink'),
      (p('matrix','Human Loop','Corrections'),p('hans','Durable Work','Hans Queue'),'follow-up','pink'),(p('security','Effect Authority','No Auto-Merge'),p('gitfabric','Release Discipline','Merge Gate'),'guards','red'),
      (p('observability','Alerts','Blocker Alert'),p('hans','Durable Work','Hans Queue'),'resumes','amber'),(p('integrations','Git Forges','GitHub'),p('gitfabric','Repository Layer','Branches / PRs'),'hosts','blue'),
      (p('lifecycle','Verify','Visual QA'),p('research','Visual Validation','Render'),'delegates','green'),(p('lifecycle','Verify','Tribunal'),p('tribunal','Review Intake','Review Request'),'challenges','green'),
      (p('company','Product & Design','Requirements'),p('openspec','Specification','Proposal'),'defines','pink'),(p('company','Engineering','Software Delivery'),p('execution','Agent Fleet','Workers'),'uses','blue'),
      (p('research','Analysis','Adversarial Research'),p('tribunal','Independent Reviewers','Risk / Security'),'evidence','violet'),(p('research','Promotion','Promote to Hans'),p('hans','Knowledge Core','Canonical Homes'),'promotes','green'),
    ]
    for a,b,label,color in E:L.append(f'{a} -> {b} "{label}" {{ color: {color} }}')

    core=['entry','hans','agent','oam','tribunal','openspec','skills','browser','matrix','gitfabric','evidence','execution','observability','security','lifecycle']
    L += ['','view landscape {','  title "⚡ Hans + Agent-Concept + Omni Audio Matrix + Tribunal"','  only '+', '.join(core),'  context off','  legend auto','  titleblock {','    subtitle: "Git-first · Skills · Audio · Tribunal · Evidence · Enterprise"','    version: "2026-09-05"','    owner: "Martin"','  }','  note top-right "Click a system for detail. HTML is canonical; screenshots are QA evidence." { style: info }','  layout {','    direction down','    density compact','    lines orthogonal','    rows [entry hans agent oam matrix]','    rows [tribunal openspec execution evidence lifecycle]','    rows [gitfabric skills browser observability security]','  }','}','']

    L += ['view ecosystem {','  title "Full Ecosystem — All Systems"','  include *','  context off','  legend auto','  layout {','    direction down','    density compact','    lines orthogonal','    rows [entry hans agent oam tribunal openspec]','    rows [skills browser matrix gitfabric evidence execution]','    rows [observability security integrations lifecycle company research]','  }','}','']

    for sid,label,_,_,_ in SYSTEMS:
        L += [f'view {sid} {{',f'  title "{label} — Detail"',f'  scope {sid}','  context off','  expand *','  legend auto','  layout {','    direction right','    density compact','    lines orthogonal','  }','}','']

    curated={
      'endtoend':('End-to-End — Issue → Integration → Knowledge',['entry','agent','openspec','tribunal','evidence','execution','gitfabric','hans','lifecycle'],[['entry','agent','openspec'],['tribunal','evidence','execution'],['gitfabric','hans','lifecycle']]),
      'controlplane':('Control Plane — Claims, Authority, Review, Status',['entry','agent','tribunal','gitfabric','security','observability','lifecycle'],[['entry','agent','tribunal'],['gitfabric','security','observability','lifecycle']]),
      'audioflow':('Audio Intelligence — Capture → Context → Review → Hans',['oam','evidence','tribunal','hans','browser','matrix'],[['oam','evidence'],['tribunal','hans'],['browser','matrix']]),
      'visualqa':('Visual Architecture QA — Squinch → HTML → Screenshots → Vision → Iterate',['skills','browser','research','evidence','gitfabric','tribunal'],[['skills','browser'],['research','evidence'],['gitfabric','tribunal']]),
      'enterprise':('Enterprise Departments & Delivery',['company','hans','agent','openspec','execution','security','observability','tribunal'],[['company','hans','agent','openspec'],['execution','security','observability','tribunal']]),
      'knowledgeflow':('Knowledge & Research Flow',['research','evidence','tribunal','hans','lifecycle','company'],[['research','evidence'],['tribunal','hans'],['lifecycle','company']]),
    }
    for name,(title,items,rows) in curated.items():
        L += [f'view {name} {{',f'  title "{title}"','  only '+', '.join(items),'  context off','  legend auto','  layout {','    direction down','    density compact','    lines orthogonal']
        for row in rows:L.append('    rows ['+' '.join(row)+']')
        L += ['  }','}','']

    engineering=['hans','agent','oam','tribunal','openspec','gitfabric','evidence','security']
    L += ['view engineeringcore {','  title "Engineering Core — Expanded"','  only '+', '.join(engineering),'  context off','  expand *','  legend auto','  note top-right "Large engineering inspection view; use scoped views for local work." { style: warning }','  layout {','    direction down','    density compact','    lines orthogonal','  }','}','']

    L += ['view everything {','  title "🧬 Everything — All Top-Level Systems"','  include *','  context off','  legend auto','  note top-right "All systems at landscape altitude. Open individual systems for full internals." { style: info }','  layout {','    direction down','    density compact','    lines orthogonal','    rows [entry hans agent oam tribunal openspec]','    rows [skills browser matrix gitfabric evidence execution]','    rows [observability security integrations lifecycle company research]','  }','}']
    out.write_text('\n'.join(L)+'\n')
    print(f"generated {out} lines={len(L)} systems={len(SYSTEMS)} containers={len(SYSTEMS)*4} leaves={len(SYSTEMS)*12} curated_views={len(curated)}")

if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('-o','--output',default='build/mega/tribunal-mega.squinch');a=ap.parse_args();o=Path(a.output);o.parent.mkdir(parents=True,exist_ok=True);emit(o)
