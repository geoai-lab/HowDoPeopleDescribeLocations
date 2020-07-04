
import re


# regular expression for identifying the tweets that contain specific locations
def regLoc(text):
    regex= r'[0-9A-Za-z]+\s(rd|ave|Street|Avenue|Road|Yard|Lane|Court|Hill|Highwalk|Way|Square|Walk|Park|Underground|Passage|Alley|Close|Gardens|Hall|Circle|Row|Buildings|Crescent|Market|Drive|Arcade|Esplanade|Grove|Garden|Bridge|Ridge|Terrace|Boulevard|Inn|Wharf|St|Ave|Rd|Yd|Ct|Pl|Sq|Bld|Blvd|Cres|Dr|Esp|Grn|Gr|Tce|Bvd|street|avenue|road|yard|lane|court|square|park|underground|building|Wall|wall|crescent|drive|esplanade|garden|bridge|ridge|terrace|boulevard|Building|grove|underground)\b'

    locations = re.finditer(regex,text)
    
    # remove some general references, e.g., "his street", "empty streets", that do not refer to specific locations
    listOfStrings = ['his' , 'the', 'a', 'my', 'never', 'from','in',r'that''s','called','for','to',
                    'at','with','of','minor','own','against','front','that','make','grave','were',
                    'busy','apartment','not','worst','watering','temporary','are','is','and','about',
                    'know','flooded','your','access','service','secret','gotta','whole','this','their',
                    'shit','save','reports','posted','possible','parallel','outside','our','or','observe',
                    'one','on','no','neighbours','multiple','localized','like','its','impacted','her',
                    'hazardous','every','empty','dear','come','by','gotta','of','stop','much','don\'t','reported','before','after']
    
    loc = []
    for m in locations:
        if m.group(0).partition(' ')[0].lower() not in listOfStrings:
            loc.append(m.group().title())
    
    return loc
