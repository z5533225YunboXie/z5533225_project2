f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}

remove = []
for suburb in f_suburbs:
    if not suburb.startswith("F"):
        remove.append(suburb)

for suburb in remove:
    f_suburbs.remove(suburb)

specified_suburbs = [
    'Fairfield', 'Fairfield East', 'Fairfield Heights', 'Fairfield West',
    'Fairlight', 'Fiddletown', 'Five Dock', 'Flemington', 'Forest Glen',
    'Forest Lodge', 'Forestville', 'Freemans Reach', 'Frenchs Forest', 'Freshwater'
]

f_suburbs.update(specified_suburbs)

print(f_suburbs)