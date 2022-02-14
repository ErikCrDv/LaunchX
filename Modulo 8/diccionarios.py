
from matplotlib.pyplot import polar


planet = {
    'name': 'Mars',
    'moons': 2
}

print( planet.get('name') )
print( planet['moons'] )

planet.update({ 'circunferencia': { 'polar': 6792 } })
planet['circunferencia']['equatorial'] = 6792

print( planet['circunferencia']['polar'] )
print( planet['circunferencia']['equatorial'] )


print( f'El planeta { planet["name"] } tiene una circunferenacia polar de { planet["circunferencia"]["polar"]}' )