text =  "Interesting facts about the Moon. The Moon is Earth's only satellite. There are several interesting facts about the Moon and how it affects life here on Earth. On average, the Moon moves 4cm away from the Earth every year. This yearly drift is not significant enough to cause immediate effects on Earth. The highest daylight temperature of the Moon is 127 C."
wordsToFind = ['average', 'temperature', 'distance']

textDividido = text.split('. ')
for oracion in textDividido:
    # print( oracion ) 

    for word in wordsToFind:

        if oracion.endswith('C.'):
            oracion = oracion.replace('C.', 'Celsius')
        if oracion.find( word ) != -1:
            print( f'En la oracion: "{ oracion }" existe la parabra "{ word }"' )

    
