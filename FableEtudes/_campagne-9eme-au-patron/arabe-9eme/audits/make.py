import sys
tpl=open('audit-tpl.md').read()
ID=sys.argv[1]; slugs=sys.argv[2:]
nums=[s.split('-')[0] for s in slugs]
out=(tpl.replace('__CHS__', ', '.join(f'`{s}`' for s in slugs))
        .replace('__RE__', '|'.join(nums))
        .replace('__CH2__', ','.join(nums))
        .replace('__ID__', ID)
        .replace('__POINTS__', open(f'points-{ID}.md').read().rstrip()))
open(f'audit-{ID}.md','w').write(out)
print(f'audit-{ID}.md', len(out))
