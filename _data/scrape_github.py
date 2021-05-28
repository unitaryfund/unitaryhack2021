from github import Github
import yaml
import os
from datetime import datetime

# using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

participating_projects = ["unitaryfund/mitiq", "PennyLaneAI/pennylane","XanaduAI/strawberryfields","XanaduAI/thewalrus",
                          "vprusso/toqito","scirate/scirate","tqsd/QuNetSim","Interlin-q/Interlin-q","pedrorrivero/qrand",
                          "vm6502q/qrack","qutip/qutip","pasqal-io/Pulser","ornl-qci/qcor", "eclipse/xacc",
                          "QuantumBFS/Yao.jl","qosf/monthly-challenges","dde/qqcs", "microsoft/qsharp-compiler"]
bountied_issues = {"unitaryfund/mitiq":[529,489,357,275,590], "PennyLaneAI/pennylane":[1225],
                   "XanaduAI/strawberryfields":[574], "XanaduAI/thewalrus":[214], "vprusso/toqito":[5,44,45],
                   "scirate/scirate":[429,430], "tqsd/QuNetSim":[82,90,52,91], "Interlin-q/Interlin-q":[35],
                   "pedrorrivero/qrand":[1,2,3], "vm6502q/qrack":[678,397], "qutip/qutip":[799,1502,1503,1160],
                   "pasqal-io/Pulser":[16,147,149], "ornl-qci/qcor":[123,101,126,129], "eclipse/xacc":[441,442,437],
                   "QuantumBFS/Yao.jl":[280,279,278], "qosf/monthly-challenges":[33,34],"dde/qqcs":[15,16,18], 
                   "microsoft/qsharp-compiler":[1028,1031,1032,1030,1033,1034]}
tags = ["[unitaryHACK]", "[unitaryhack]", "[UnitaryHACK]", "[UnitaryHack]"]
participating_repos = { project : g.get_repo(project) for project in participating_projects }

def format_as_yaml(results:dict, include_empty=False, header=""):
    return "# " + header + "\n" + yaml.dump(
        [{'name' : k, 'data' : v} for k, v in results.items() if ((v!=[]) or include_empty)], 
        sort_keys=False, explicit_start=True, width=50, indent=2)

def unitary_hack_labeled_issues(participating_repos, attribute="title",status="open"):
    issues = {}
    for name, project in participating_repos.items():
        project_issues = project.get_issues(state=status, sort='created', labels=['unitaryhack'])
        issues[name] = [getattr(i, attribute) for i in project_issues] 
    return issues

def unitary_hack_prs(participating_repos, attribute="title", state="open"):
    prs = {}
    for name, project in participating_repos.items():
        pulls = project.get_pulls(state=state, sort='created')
        prs[name] = [getattr(pr, attribute) for pr in pulls if any(x in pr.title for x in tags)] 
    return prs

def unitary_hack_prs_yaml(participating_repos, state="open", merged=False):
    prs = {}
    for name, project in participating_repos.items():
        pulls = project.get_pulls(state=state, sort='created')
        prs[name] = [{'title': pr.title, 'number': pr.number, 'user': pr.user.login} for pr in pulls 
                             if (any(x in pr.title for x in tags) and (pr.merged==merged))] 
    
    with open(("merged" if merged else "open") + "-prs.yaml", "w") as f:
        print(format_as_yaml(prs, 
            header=f"updated: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"), 
            file=f
        )
    
def unitary_hack_bounties_yaml(participating_repos, bountied_issues, state="open"):    
    bounties = {}
    for name, project in participating_repos.items():
        project_bounties = [project.get_issue(num) for num in bountied_issues[name]]
        bounties[name] = [{'title': i.title, 'number': i.number, 'user': i.user.login} for i in project_bounties 
                             if i.state==state] 
    
    with open(state + "-bounties.yaml", "w") as f:
        print(format_as_yaml(bounties, 
            header=f"updated: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"), 
            file=f
        )
print("Checking for pending PRs...")
unitary_hack_prs_yaml(participating_repos, state="open", merged=False)
print("Checking for merged PRs...")
unitary_hack_prs_yaml(participating_repos, state="closed", merged=True)
print("Checking for open bounties...")
unitary_hack_bounties_yaml(participating_repos, bountied_issues, state="open")
print("Checking for closed bounties...")
unitary_hack_bounties_yaml(participating_repos, bountied_issues, state="closed")
print("Done! ♥")
