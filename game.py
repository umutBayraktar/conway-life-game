
def parseInput(input_string):

    if input_string == '' or input_string is None:
        return 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz'

    if ',' in input_string:
        parsed_input=input_string.split(',')
        if len(parsed_input) != 2:
            return 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz'
        else: #len == 2 x,y
            try:
                x = int(parsed_input[0])
                y = int(parsed_input[1])
                if x < 0 or y < 0:
                    return 'İndis değeri negatif olamaz'
                elif x > 7 or y >7:
                    return 'İndis değeri 7 den büyük olamaz'
                return {'x':x,'y': y}
            except:
                return 'Lütfen nümerik veri giriniz'




    else:
        return 'Yanlış girdi,lütfen koordinat bilgisini x,y şeklinde giriniz'


