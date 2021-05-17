from github import Github
import yaml
import os

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

def format_as_yaml(results:dict, include_empty=False):
    return yaml.dump([{'name' : k, 'data' : v} for k, v in results.items() if ((v!=[]) or include_empty)], sort_keys=False,explicit_start=True,width=50, indent=2)

def unitary_hack_labeled_issues(participating_projects, atribute="title",status="open"):
    open_issues = {}
    for project in participating_projects:
        issues = g.get_repo(project).get_issues(state=status, sort='created', labels=['unitaryhack'])
        open_issues[project] = [getattr(i, atribute) for i in issues] 
    return open_issues

def unitary_hack_prs(participating_projects, atribute="title", status="open"):
    open_prs = {}
    for project in participating_projects:
        pulls = g.get_repo(project).get_pulls(state=status, sort='created')
        open_prs[project] = [getattr(pr, atribute) for pr in pulls if '[unitaryHACK]' in pr.title] 
    return open_prs

def unitary_hack_prs_yaml(participating_projects, state="open", merged=False):
    open_prs = {}
    for project in participating_projects:
        pulls = g.get_repo(project).get_pulls(state=state, sort='created')
        open_prs[project] = [{'title': pr.title, 'number': pr.number} for pr in pulls 
                             if (('[unitaryHACK]' in pr.title) and (pr.merged==merged))] 
    with open(("merged" if merged else "open") + "-prs.yaml", "w") as f:
        print(format_as_yaml(open_prs), file=f)
    
def unitary_hack_bounties_yaml(participating_projects, bountied_issues, state="open"):    
    bounties = {}
    for project in participating_projects:
        project_bounties = [g.get_repo(project).get_issue(num) for num in bountied_issues[project]]
        bounties[project] = [{'title': i.title, 'number': i.number} for i in project_bounties if i.state==state] 
    with open(state + "-bounties.yaml", "w") as f:
        print(format_as_yaml(bounties), file=f)

unitary_hack_prs_yaml(participating_projects, merged=False)
unitary_hack_prs_yaml(participating_projects, merged=True)
unitary_hack_bounties_yaml(participating_projects, bountied_issues, state="open")
unitary_hack_bounties_yaml(participating_projects, bountied_issues, state="closed")