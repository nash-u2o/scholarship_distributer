import random


def act():
    return random.randint(15, 36)


def church():
    r = random.randint(1, 100)
    if r < 10:
        return None
    return random.choice(
        [
            "mars hill pentecostal church",
            "cedar lake church",
            "capstone community church",
            "life church",
            "liberty",
            "fountain of life church",
            "first baptist church",
            "west mccomb baptist church",
            "first baptist church zachary",
            "bluff creek baptish church",
            "the church at brookhills",
            "north highland baptist church",
            "rock hill mb church",
            "true vine christian baptist church",
            "vineyard jackson",
            "the station church",
            "first baptist church florence",
            "pinelake church",
            "first baptist church-dallas",
            "cade chaple",
            "all things new worship center",
            "hope church",
            "3circle church",
            "word of life",
            "collierville first baptist church",
            "brownsville missionary baptist church",
            "colonial heights baptist church",
            "zion travelers mb church",
            "riveroaks reformed presbyterian church",
            "jefferson baptist church",
            "first baptist church of opelika",
            "amite baptist",
            "bartaria baptist church",
            "healing place church",
            "magnolia first united methodist church",
            "morton church of christ",
            "barnett independent church",
            "northwood church",
            "bellwether church",
            "freeny baptist church",
            "hebron church",
            "new good hope baptist church",
            "the northview churh",
            "grace community church",
            "pathway church",
            "great st james baptist church",
            "first baptist church of rayville",
            "salem baptist church",
            "st. joseph catholic church",
            "fellowship baptist church",
            "purvis methodist church",
            "longview point baptist church",
            "pleasant ridge baptist church",
            "st. alphonsus",
            "immanuel presbyterian church",
            "calvary baptist church",
            "sardis baptist church",
            "harmonia congregational methodist church",
            "itawamba christian church",
            "grace church",
            "clear branch baptist church",
            "heucks retreat baptist church",
            "first baptist church jackson",
            "first assembly of god",
            "hernando methodist church",
            "crossroads baptist church",
            "evangel pca",
            "venture church",
            "smithville baptist church",
            "parkview baptist church",
            "morrison heights baptist church",
            "first presbyterian jackson",
            "first baptist church flora",
            "renewal church",
            "fuente de agua viva",
            "canton christian center",
            "flowood baptist church",
            "philadelphia baptist church",
            "the salvation army",
            "truitt memorial baptist church",
            "germantown baptist church",
            "broadmoor baptist church",
            "parks baptist church",
            "church of the king",
            "new jerusalam progressive cogic",
            "pear orchard presbyterian church",
            "grace presbyterian church",
            "first baptist church  saltillo",
            "mount helm baptist church",
            "st. mark's episcopal",
            "union baptist church",
            "crossway church",
            "cliff temple baptist church",
            "first pentecostal church",
            "grace crossing baptist church",
            "first baptist church water valley",
            "church of the highlands",
            "first new testament church",
            "ludlow baptist church",
            "brandon baptist church",
            "hurley methodist church",
            "new jerusalem church",
            "crosspoint church",
            "saint alban's episcopal church",
            "new zion baptist church",
            "seven day adventist hispanic church",
            "crossgates baptist church",
            "st. alphonsus catholic church",
            "hickory ridge baptist church",
            "bartlett baptist church",
            "sand hill baptist church",
            "park place baptist church",
            "new hope baptist church",
            "first baptist church of rayville, louisiana",
            "new liberty baptist church",
            "word of life church",
            "crawford street united methodist church",
            "parkway baptist church",
            "first baptist church picayune",
            "heritage baptist church",
            "northeast church of christ",
            "high point church",
            "fruit cove baptist church",
            "tate baptist church",
            "mclaurin heights baptist church",
            "westminster presbyterian church",
            "new beginnings church",
            "northcrest baptist church",
            "oakdale baptist church",
            "elevate",
            "new bethel missionary baptist church",
            "russell baptist church",
            "first christian church",
            "cropwell baptist",
            "providence baptist church",
            "hernando baptist church",
            "whitedove fellowship",
            "antioch baptist church",
            "mount hermon baptist church",
            "springhill baptist church",
            "zion travelers",
            "good hope baptist church",
            "epicenter church",
            "warren community church",
            "madden baptist church",
            "pocahontas baptist church",
            "auburn community church",
            "grace life church of brookhaven",
            "westminster presbyterian church (pca)",
            "kingdom hall of jehovah's witness",
            "mt hood missionary baptist church",
            "immanuel baptist church",
            "crossgates united methodist church",
            "lakeland presbyterian church",
            "newell chapel",
            "first baptist madison",
            "saint hilary of pointers",
            "touro synagogue",
            "nathas ministries word of god's church",
            "ressurection life",
            "holy savior catholic church",
            "woodlawn baptist church",
            "new jerusalem",
            "3 circle",
            "saint elizabeth seton",
            "first presbyterian church of hattiesburg",
            "heart church",
            "journey community church",
            "star baptist church",
            "fbc clinton",
            "bethel baptist church",
            "spring hill mb church",
            "none",
            "christ fellowship church of magee",
            "bay springs baptist church",
            "woolmarket baptist church",
            "evangelist temple church - god",
            "the orchard",
            "redeemer",
            "the gathering church",
            "lebanon presbyterian church",
            "fearns chapel church",
            "mt tabor missionary baptist church",
            "woodland presbyterian church",
            "anding baptist church",
            "grace primitive baptist church",
            "cornerstone",
            "zion chapel ame church",
            "damascus baptist church",
            "st matthews catholic church",
            "westminster pca",
            "lake road chapel, keswick, cumbria, united kingdom",
            "apostolic church of jesus",
            "venture baptist",
            "cherry grove baptsit church",
            "midtree church",
            "covenant church",
            "grace baptist church",
            "highland baptist church",
            "first united methodist church clinton",
            "providence presbyterian church",
            "st. joseph's catholic church",
            "micheal memorial",
            "harvestpoint church",
            "house of god",
            "saint peter church of god in christ",
            "pine bluff baptist church",
            "cornerstone church southaven",
            "first baptist church tupelo",
            "new mount calvary christian center",
            "mosaic church",
            "rocky creek baptist church",
            "church at viera",
            "rosepark baptist church",
            "calvary united methodist church",
            "quan am tinh vien",
            "memorial united methodist church",
            "monticello baptist church",
            "first presbyterian church jackson ms",
            "grace covenant church",
            "church of jesus christ of latter-day saints",
            "superior avenue baptist church",
            "riverwood bible church",
            "evergreen methodist church",
            "hope church tupelo",
            "springfield baptist church",
            "first presbyterian church",
            "thorington road baptist",
            "pine lake baptist church",
            "st. bede catholic church",
            "corinth baptist church",
            "westly chapel",
            "harrisburg baptist church",
            "north oxford baptist church",
            "greater bethlehem temple",
            "eastwood baptist church",
            "world overcomer's ministries",
            "st. mary's catholic church",
            "cade chapel missionary bapyist church",
            "bethesda baptist church",
            "bible baptist church",
            "highlands presbyterian church",
            "double oak community church",
            "salem lutheran church",
            "3 circle church",
            "faith baptist church",
            "first baptist church fannin",
            "lakeshore church",
            "eagle lake baptist church",
            "redemption church",
            "st. timothy",
            "first presbyterian",
            "first baptist church of kenner",
            "crossgate bible church",
            "forest baptist church",
            "naples independent baptist church",
            "kingdom hall of jehovah witnesses",
            "temple baptist church",
            "trinity church",
            "house of refuge church",
            "independent presbyterian church",
            "west heights baptist church",
            "flora methodist",
            "mt. carmel ministries",
            "pearson baptist church",
            "mount zion baptist church",
            "redeemer church, pca",
            "saint richards catholic church",
            "enon cumberland presbyterian church",
            "our lady of prompt succor",
            "church of christ",
            "relate",
            "memphis grace of the nazarene",
            "henderson church of christ",
            "st francis of assisi",
            "the way church",
            "west jackson street baptist church",
            "hopewell baptist church",
            "compel church olive branch campus",
            "spanish fort united methodist church",
            "first baptist church montgomery",
            "first baptist",
            "bethlehem m.b. church",
            "riveroaks presbyterian church",
            "holy trinity catholic church",
            "pine grove baptist church",
            "little bethel cme church",
            "lagoinha orlando church",
            "new vision prayer assembly",
            "southwood presbyterian church, pca",
            "morton church of god",
            "old mt calvary baptist church",
            "christ church crossroads",
            "quan am tinh vien temple",
            "whitesburg baptist church",
            "briarwood presbyterian church, pca",
            "the israel of god",
            "soild rock",
            "hilltop",
            "city of refuge church of god in christ",
            "crossgates baptist",
            "the exchange",
            "new life saline county",
            "trinity bible church",
            "first baptist church of florence",
            "reformation presbyterian church",
            "mt. pisgah baptist church-ob",
            "new covenant family worship center",
            "bethlehem church",
            "pleasant valley baptist church",
            "deliverance tabernacle church",
            "first cumberland presbyterian church",
            "progressive missionary baptist church",
            "fellowship church",
            "pinelake madison",
            "longview heights baptist church",
            "desoto hills baptist church",
            "shades mountain community church",
            "harvest memphis",
            "gaston baptist church",
            "first baptist church bronston",
            "south louisville baptist church",
            "shady grove babtist church",
            "word and worship",
            "emmanuel baptist church",
            "fondren church",
            "rivertree",
            "first independent methodist church",
            "fellowship of the parks",
            "fbc madison",
            "compel church",
            "mercy hill community church",
            "liberty baptist church",
            "pilgrims rest missionary baptist church",
            "greater pearlie grove",
            "lakeside baptist church",
            "new zion christian faith church",
            "salem missionary baptist church",
            "sunset view baptist church",
            "mosaic",
            "calvary christian oak forest bapt",
            "middlebrook united methodist church",
            "riverside baptist church",
            "the pointe",
            "meadowgroove",
            "highland colony baptist church",
            "first baptist church of collinsville",
            "briar hill baptist church",
            "bellevue baptist church memphis, tn",
            "crestview congregational methodist",
            "rock hill m.b church",
            "iglesia penecostal bethel",
            "mount center missionary baptist church",
            "first presbyterian church of ocean springs",
            "gatesville baptist church",
            "wynndale baptist church",
            "grace evangelical",
            "james river church",
            "hays creek church",
            "saint paul catholic church",
            "proximity christian fellowship",
            "greater mt lebanon m.b church",
            "king solomon baptist church",
            "greater belmont mb church",
            "cato baptist church",
            "fbc bruce",
            "st.james",
            "bellevue baptist church",
            "cedar lake christian assembly",
            "pine lake",
            "first baptist jennings",
            "the community church",
            "st lawrence catholic church",
            "riverside community church",
            "world overcomers church",
            "luther memorial church",
            "upon this rock ministry",
            "firstbaptist church starkville",
            "calvary presbyterian church",
            "black's chapel m.b. church",
            "first united methodist church of clinton",
            "first true love world outreach ministry",
            "williamsville baptist church",
            "lakeridge methodist church",
            "new home church of christ holiness usa",
            "st. marks methodist church",
            "bartlett baptist",
            "prattville first methodist church",
            "embrace church",
            "mount helm baptist chruch",
            "pleasant hill baptist church",
            "new mount calvery christian center",
            "macedonia primitive baptist church",
            "st. clement of rome",
            "hebron baptist church",
            "neighborhood church",
            "gardendale first baptist church",
            "central churucj",
            "bolton united methodist",
            "journey church",
            "cross community church",
            "fifteenth avenue baptist church",
            "bryant lane cowboy church",
            "north greenwood baptist church",
            "meadowbrook church",
            "hurley global methodist church",
            "wellspring community church",
            "country woods baptist church",
            "wanilla baptist church",
            "the life church",
            "carr's chapel church",
            "first presbyterian church of jackson ms",
            "homewood baptist church",
            "west corinth baptist church",
            "heidelberg presbyterian",
            "covenant presbyterian church",
            "faith baptist bartlett",
            "north winona baptist chruch",
            "bethlehem mb church",
            "hill chapel missionary baptist church",
            "the bridge",
            "old union baptist church",
            "freedom rock",
            "west union baptist church",
            "evangel",
            "harvest international ministry",
            "college hill baptist",
            "clarkson baptist church",
            "michael memorial baptist church",
            "crossgates united methodist",
            "spring hill baptist church",
            "gracewood baptist church",
            "wyatte baptist church",
            "first baptist church branson",
            "lemoyne boulevard baptist church",
            "rivertree church",
            "cross roads baptist church",
            "hall's freewill baptist church",
            "destiny church",
            "st richard catholic church",
            "trinity presbyterian pca",
            "first baptist church lyman",
            "utica christian church",
            "oak park baptist church",
            "bellwether",
            "assembly of god strong tower",
            "new bethel baptist church",
            "covenant baptist church",
        ]
    )


def county():
    return random.choice(
        [
            "neshoba",
            "harrison",
            "tuscaloosa",
            "franklin",
            "baldwin",
            "mobile",
            "saint tammany",
            "pike",
            "east baton rouge",
            "amite",
            "shelby",
            "jefferson",
            "rankin",
            "kaufman",
            "hinds",
            "washington",
            "lee",
            "madison",
            "livingston",
            "copiah",
            "clarke",
            "leake",
            "barrow",
            "scott",
            "fulton",
            "desoto",
            "richland",
            "smith",
            "lamar",
            "tate",
            "calhoun",
            "holmes",
            "itawamba",
            "wichita",
            "fayette",
            "hancock",
            "leflore",
            "monroe",
            "jones",
            "lincoln",
            "union",
            "warren",
            "jasper",
            "jackson",
            "walthall",
            "adams",
            "yalobusha",
            "covington",
            "attala",
            "yazoo",
            "pearl river",
            "autauga",
            "santa rosa",
            "saint johns",
            "alcorn",
            "forrest",
            "lauderdale",
            "lafayette",
            "colorado",
            "saint clair",
            "henry",
            "lafourche",
            "orleans",
            "sunflower",
            "surry",
            "sharkey",
            "lowndes",
            "george",
            "harris",
            "brevard",
            "bossier",
            "benton",
            "east feliciana",
            "montgomery",
            "simpson",
            "hillsborough",
            "collier",
            "pontotoc",
            "choctaw",
            "rutherford",
            "elmore",
            "kenosha",
            "saline",
            "parker",
            "prentiss",
            "escambia",
            "ascension",
            "clay",
            "winston",
            "midland",
            "denton",
            "spotsylvania",
            "greene",
            "bryan",
            "stone",
            "chickasaw",
            "jefferson davis",
            "martin",
            "oktibbeha",
            "lubbock",
            "marion",
            "milwaukee",
            "crittenden",
            "carroll",
            "lawrence",
            "panola",
            "webster",
            "newton",
        ]
    )


def gender():
    r = random.randint(1, 100)
    if r >= 40:
        return "female"
    return "male"


def gpa():
    return round(random.uniform(2.00, 4.00) * 100) / 100


def high_school():
    return random.choice(
        [
            "carthage christian academy",
            "christian collegiate academy",
            "northside high school",
            "newton high school",
            "franklin parish high school",
            "elberta high school",
            "saraland high school",
            "northlake christian school",
            "mississippi school of the arts",
            "zachary high school",
            "silliman institute",
            "evangel christian school",
            "mortimer jordan high school",
            "mclaurin attendance center",
            "florence high school",
            "brandon high school",
            "hoover high school",
            "northwest rankin high school",
            "forney high school",
            "forest hill high school",
            "chipley high school",
            "tupelo high school",
            "fairhope high school",
            "collierville high school",
            "hinds community college-admissions and records",
            "holmes community college",
            "westminster academy",
            "denham springs high school",
            "southern union state community college: opelika campus",
            "parkview baptist high school",
            "copiah-lincoln community college",
            "live oak high school",
            "parkview baptist school",
            "fisher middle high school",
            "southwest mississippi community college",
            "jones county junior college",
            "mississippi gulf coast community college",
            "belhaven university",
            "east central community college",
            "homeschool",
            "morton high school",
            "homeschool (please choose this one if home schooled)",
            "homeschool (please choose this one)",
            "blue mountain christian university",
            "riverfield academy",
            "ascension christian high school",
            "pearl river community college-poplarville",
            "mississippi valley state university",
            "northwest mississippi community college",
            "pearl river community college",
            "mississippi college",
            "tupelo christian preparatory school",
            "saint augustine school",
            "itawamba community college",
            "wichita falls high school",
            "university of memphis",
            "delta state university",
            "madison central high school",
            "evangel classical christian school",
            "pillow academy",
            "homelife academy",
            "hillcrest high school",
            "evangelical christian school",
            "northeast mississippi community college",
            "university of southern mississippi",
            "clinton high school",
            "saint andrew's episcopal school",
            "st. patrick catholic high school",
            "puckett high school",
            "crossroads christian school",
            "homeschooled",
            "washington school",
            "hewitt-trussville hs",
            "unified homeschool",
            "clinton christian academy",
            "mississippi gulf coast community college: perkinston",
            "prattville high school",
            "gulf breeze high school",
            "providence extension program--homeschool cooperative",
            "presbyterian christian high school",
            "meridian community college",
            "pineda acadamy of excellence",
            "union university",
            "pell city high school",
            "pearl high school",
            "community college of the air force - registrars division",
            "crescent city christian school",
            "mount hermon high school",
            "southwest tennessee community college",
            "purvis high school",
            "fayette academy",
            "oak mt. high school",
            "tougaloo college",
            "ridgeland high school",
            "mississippi delta community college",
            "central lafourche high school",
            "isidore newman school",
            "a beka academy: traditional parent directed program for home school",
            "birmingham-southern college",
            "ocean springs high school",
            "sharkey-issaquena academy",
            "east mississippi community college",
            "presbyterian christian school",
            "george county high school",
            "wingfield high school",
            "william carey university",
            "mcgill-toolen catholic high school",
            "keswick school",
            "elysian fields high school",
            "classical conversations homeschool",
            "shades mountain independent church academy",
            "saint lukes episcopal school-middle-upper campus",
            "germantown high school",
            "lewisburg high school",
            "satellite high school",
            "benton high school",
            "neshoba central high school",
            "ben's ford christian school",
            "great teachers condor",
            "mooreville high school",
            "homelife academy homeschool",
            "alabama christian academy",
            "montgomery catholic preparatory school",
            "mississippi state university",
            "madison ridgeland academy (mra)",
            "rebul academy",
            "chelsea high school",
            "jackson academy",
            "east rankin academy",
            "tampa catholic high school",
            "john curtis christian school",
            "rb homeschool",
            "hartfield academy",
            "saint thomas more catholic high school",
            "vicksburg catholic-saint aloysius catholic high school",
            "freed-hardeman university",
            "spanish fort high school",
            "blue mountain university",
            "ezekiel academy",
            "hancock high school",
            "homestead high school",
            "southeastern baptist college",
            "alcorn state university - registrar's office",
            "west orange high school",
            "huntsville high school 35801",
            "gateway technical college",
            "huntsville high school",
            "vestavia hills high school",
            "jackson preparatory school",
            "bryant high school",
            "aledo high school",
            "pike road junior senior high school",
            "regents school of oxford",
            "j m tate high school",
            "briarwood christian high school",
            "northpoint christian school",
            "somerset community college",
            "mize attendance center",
            "laurel christian school",
            "whitesburg christian academy",
            "saltillo high school",
            "oak hill academy",
            "helena high school",
            "the university of mississippi",
            "park place christian academy",
            "durant high school",
            "north pike high school",
            "raymond high school",
            "home life academy, jackson, tn, 38305",
            "faith heritage christian academy",
            "winona secondary school",
            "ritter homeschool",
            "clarkdale high school",
            "lake arthur high school",
            "columbus girls school of excellence",
            "saint michael catholic high school",
            "university of south carolina: columbia",
            "olive branch high school",
            "river falls high school",
            "starr's mill high school",
            "hopkinsville community college",
            "frenship high school",
            "bevill state community college",
            "blue mountain college",
            "california virtual academy san diego",
            "tri-county academy",
            "haleyville high school",
            "wenatchee valley college",
            "ged (high school equivalency)",
            "west lauderdale high school",
            "lawrence county high school",
            "growing in grace",
            "arkansas state university midsouth",
            "rhodes college",
            "french camp",
            "desoto central high school",
            "donoho school",
            "saint pauls episcopal school",
            "school of the ozarks",
            "saint martin high school",
            "virgil i grissom high school",
            "university of west alabama",
            "home school",
            "bogue chitto school",
            "westminster school at oak mountain",
            "brookhaven academy",
            "reedy high school",
        ]
    )


def major():
    return random.choice(
        [
            "music",
            "biology",
            "business",
            "pre-med",
            "nursing",
            "english",
            "christian studies",
            "chemistry",
            "math",
            "journalism",
            "education",
            "science",
            "computer science",
            "art",
            "kinesiology",
            "history",
            "political science",
            "social science",
            "design",
            "social work",
            "engineering",
            "communication",
            "modern languages",
            "undecided",
        ]
    )


def married():
    r = random.randint(1, 100)
    if r == 1:
        return "yes"
    return "no"


def ministry():
    r = random.randint(1, 100)
    if r <= 10:
        return "yes"
    return "no"
    pass


def ministry_dependent():
    r = random.randint(1, 100)
    if r == 1:
        return "yes"
    return "no"


def need():
    r = random.randint(1, 100)
    if r >= 50:
        return "yes"
    return "no"


def minority():
    r = random.randint(1, 100)
    if r <= 70:
        return "no"
    return "yes"


def state():
    r = random.randint(1, 100)
    if r <= 85:
        return "ms"
    return random.choice(
        [
            "al",
            "la",
            "tx",
            "fl",
            "tn",
            "ga",
            "nc",
            "wi",
            "ar",
            "ky",
            "va",
            "ok",
            "mo",
        ]
    )


# Order of attributes: id, ACT, CHURCH, COUNTY, GENDER, GPA, HIGH SCHOOL, MAJOR, MARRIED, MINISTRY, MINISTRY DEPENDENT, NEED, MINORITY, STATE
# exclude country for now
def create_student(i):
    """
    Returns:
        List of list of individual student entries
    """
    students = []
    for i in range(i + 1):
        students.append(
            [
                f"stu{i}",
                act(),
                church(),
                # county(),
                gender(),
                gpa(),
                high_school(),
                major(),
                married(),
                ministry(),
                ministry_dependent(),
                need(),
                minority(),
                state(),
            ]
        )

    return students
