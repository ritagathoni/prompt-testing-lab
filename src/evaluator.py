"""Deterministic prompt contract testing: checks responses, not model intelligence."""
import json
import re
from pathlib import Path

def assess(response, checks):
    results=[]
    for check in checks:
        kind=check['type']; expected=check.get('value'); passed=False; note=''
        if kind=='must_include':
            passed=str(expected).casefold() in response.casefold()
        elif kind=='must_not_include':
            passed=str(expected).casefold() not in response.casefold()
        elif kind=='max_words':
            passed=len(response.split())<=int(expected)
        elif kind=='min_words':
            passed=len(response.split())>=int(expected)
        elif kind=='regex':
            passed=bool(re.search(expected,response,re.MULTILINE))
        elif kind=='json_only':
            try:
                json.loads(response);passed=True
            except json.JSONDecodeError:
                passed=False
        else:
            raise ValueError('Unknown check type: '+kind)
        results.append({'type':kind,'expected':expected,'passed':passed})
    return {'passed':all(x['passed'] for x in results),'passed_checks':sum(x['passed'] for x in results),
            'total_checks':len(results),'checks':results}

def run_cases(path):
    cases=json.loads(Path(path).read_text(encoding='utf-8'))
    return [{'id':c['id'],'family':c['family'],'results':assess(c['response'],c['checks'])} for c in cases]

if __name__=='__main__':
    import sys
    path=sys.argv[1] if len(sys.argv)>1 else 'data/cases.json'
    print(json.dumps(run_cases(path),indent=2))
