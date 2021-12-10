# Generated by Django 3.1.13 on 2021-12-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('myAirport', models.CharField(choices=[('ABR', 'Aberdeen Regional Airport'), ('ABI', 'Abilene Regional Airport'), ('SPI', 'Abraham Lincoln Capital Airport'), ('CAK', 'Akron–Canton Airport'), ('ALB', 'Albany International Airport'), ('OAJ', 'Albert J. Ellis Airport'), ('ABQ', 'Albuquerque International Sunport'), ('AEX', 'Alexandria International Airport'), ('APN', 'Alpena County Regional Airport'), ('ANI', 'Aniak Airport'), ('GUM', 'Antonio B. Won Pat International Airport'), ('VQS', 'Antonio Rivera Rodríguez Airport'), ('ATW', 'Appleton International Airport'), ('ACV', 'Arcata Airport'), ('LBE', 'Arnold Palmer Regional Airport'), ('AVL', 'Asheville Regional Airport'), ('ASE', 'Aspen/Pitkin County Airport (Sardy Field)'), ('ACY', 'Atlantic City International Airport'), ('AGS', 'Augusta Regional Airport (Bush Field)'), ('AUS', 'Austin–Bergstrom International Airport'), ('BWI', 'Baltimore/Washington International Airport'), ('BGR', 'Bangor International Airport'), ('PAH', 'Barkley Regional Airport'), ('BTR', 'Baton Rouge Metropolitan Airport (Ryan Field)'), ('BLI', 'Bellingham International Airport'), ('BJI', 'Bemidji Regional Airport'), ('CPX', 'Benjamín Rivera Noriega Airport'), ('BTM', 'Bert Mooney Airport'), ('BET', 'Bethel Airport (also see Bethel Seaplane Base)'), ('BIL', 'Billings Logan International Airport'), ('BHM', 'Birmingham–Shuttlesworth International Airport'), ('FNT', 'Bishop International Airport'), ('BIS', 'Bismarck Municipal Airport'), ('BID', 'Block Island State Airport'), ('LEX', 'Blue Grass Airport'), ('BOI', 'Boise Airport (Boise Air Terminal) (Gowen Field)'), ('BLD', 'Boulder City Municipal Airport'), ('BZN', 'Bozeman Yellowstone International Airport (was Gallatin Field Airport)'), ('BDL', 'Bradley International Airport'), ('BRD', 'Brainerd Lakes Regional Airport'), ('BRO', 'Brownsville/South Padre Island International Airport'), ('BQK', 'Brunswick Golden Isles Airport'), ('CCR', 'Buchanan Field Airport'), ('BUF', 'Buffalo Niagara International Airport'), ('BTV', 'Burlington International Airport'), ('CNY', 'Canyonlands Field'), ('HYA', 'Cape Cod Gateway Airport (Boardman/Polando Field)'), ('LAN', 'Capital Region International Airport (was Lansing Capital City)'), ('CPR', 'Casper–Natrona County International Airport'), ('CDC', 'Cedar City Regional Airport'), ('BMI', 'Central Illinois Regional Airport at Bloomington-Normal'), ('GRI', 'Central Nebraska Regional Airport'), ('CWA', 'Central Wisconsin Airport'), ('RIW', 'Central Wyoming Regional Airport (was Riverton Regional)'), ('STS', 'Charles M. Schulz–Sonoma County Airport'), ('CHS', 'Charleston International Airport / Charleston AFB'), ('CLT', 'Charlotte Douglas International Airport'), ('CHO', 'Charlottesville–Albemarle Airport'), ('CHA', 'Chattanooga Metropolitan Airport (Lovell Field)'), ('TVC', 'Cherry Capital Airport (was Cherry County Airpark)'), ('MDW', 'Chicago Midway International Airport'), ('ORD', "Chicago O'Hare International Airport"), ('RFD', 'Chicago Rockford International Airport (was Northwest Chicagoland Regional Airport at Rockford)'), ('CIU', 'Chippewa County International Airport'), ('EAU', 'Chippewa Valley Regional Airport'), ('CVG', 'Cincinnati/Northern Kentucky International Airport'), ('COS', 'City of Colorado Springs Municipal Airport'), ('CLE', 'Cleveland Hopkins International Airport'), ('LIT', 'Clinton National Airport (Adams Field) (was Little Rock National)'), ('EWN', 'Coastal Carolina Regional Airport (was Craven County Regional)'), ('CAE', 'Columbia Metropolitan Airport'), ('COU', 'Columbia Regional Airport'), ('CSG', 'Columbus Airport'), ('USA', 'Concord Regional Airport'), ('CRP', 'Corpus Christi International Airport'), ('STT', 'Cyril E. King Airport'), ('DAL', 'Dallas Love Field'), ('DFW', 'Dallas/Fort Worth International Airport'), ('MSN', 'Dane County Regional Airport (Truax Field)'), ('HNL', 'Daniel K. Inouye International Airport'), ('DAB', 'Daytona Beach International Airport'), ('SCC', 'Deadhorse Airport (Prudhoe Bay Airport)'), ('ESC', 'Delta County Airport'), ('DEN', 'Denver International Airport'), ('DSM', 'Des Moines International Airport'), ('VPS', 'Destin–Fort Walton Beach Airport / Eglin Air Force Base'), ('DTW', 'Detroit Metropolitan Wayne County Airport'), ('DIK', 'Dickinson Theodore Roosevelt Regional Airport'), ('DLG', 'Dillingham Airport'), ('DHN', 'Dothan Regional Airport'), ('DBQ', 'Dubuque Regional Airport'), ('DLH', 'Duluth International Airport'), ('DRO', 'Durango–La Plata County Airport'), ('EGE', 'Eagle County Regional Airport'), ('GGG', 'East Texas Regional Airport'), ('CLL', 'Easterwood Airport (Easterwood Field)'), ('ELP', 'El Paso International Airport'), ('EKO', 'Elko Regional Airport (J.C. Harris Field)'), ('KOA', 'Ellison Onizuka Kona International Airport at Keahole'), ('ELM', 'Elmira/Corning Regional Airport'), ('OMA', 'Eppley Airfield'), ('ERI', 'Erie International Airport (Tom Ridge Field)'), ('EUG', 'Eugene Airport (Mahlon Sweet Field)'), ('EVV', 'Evansville Regional Airport'), ('FAI', 'Fairbanks International Airport'), ('INL', 'Falls International Airport'), ('FAY', 'Fayetteville Regional Airport (Grannis Field)'), ('SIG', 'Fernando Luis Ribas Dominicci Airport (Isla Grande Airport)'), ('FLG', 'Flagstaff Pulliam Airport'), ('FLO', 'Florence Regional Airport'), ('IMT', 'Ford Airport'), ('FLL', 'Fort Lauderdale–Hollywood International Airport'), ('FSM', 'Fort Smith Regional Airport'), ('FWA', 'Fort Wayne International Airport'), ('FAT', 'Fresno Yosemite International Airport'), ('FRD', 'Friday Harbor Airport'), ('SUN', 'Friedman Memorial Airport'), ('GNV', 'Gainesville Regional Airport'), ('GCK', 'Garden City Regional Airport'), ('BOS', 'Gen. Edward Lawrence Logan International Airport'), ('PIA', 'General Downing-Peoria International Airport'), ('IAH', 'George Bush Intercontinental Airport'), ('GRR', 'Gerald R. Ford International Airport'), ('GCC', 'Gillette–Campbell County Airport'), ('FCA', 'Glacier Park International Airport'), ('GTR', 'Golden Triangle Regional Airport'), ('GCN', 'Grand Canyon National Park Airport'), ('GFK', 'Grand Forks International Airport'), ('GJT', 'Grand Junction Regional Airport (Walker Field)'), ('GTF', 'Great Falls International Airport'), ('BGM', 'Greater Binghamton Airport (Edwin A. Link Field)'), ('ROC', 'Greater Rochester International Airport'), ('GRB', 'Green Bay–Austin Straubel International Airport'), ('LWB', 'Greenbrier Valley Airport'), ('GSP', 'Greenville–Spartanburg International Airport (Roger Milliken Field)'), ('GPT', 'Gulfport–Biloxi International Airport'), ('GUC', 'Gunnison–Crested Butte Regional Airport'), ('GST', 'Gustavus Airport'), ('HGR', 'Hagerstown Regional Airport (Richard A. Henson Field)'), ('BED', 'Hanscom Field / Hanscom Air Force Base'), ('MDT', 'Harrisburg International Airport'), ('ATL', 'Hartsfield–Jackson Atlanta International Airport'), ('FAR', 'Hector International Airport'), ('HLN', 'Helena Regional Airport'), ('STX', 'Henry E. Rohlsen Airport'), ('ITO', 'Hilo International Airport'), ('HHH', 'Hilton Head Airport'), ('BUR', 'Hollywood Burbank Airport (was Bob Hope Airport)'), ('HOM', 'Homer Airport'), ('CMX', 'Houghton County Memorial Airport'), ('HSV', 'Huntsville International Airport (Carl T. Jones Field)'), ('IDA', 'Idaho Falls Regional Airport (Fanning Field)'), ('IND', 'Indianapolis International Airport'), ('ITH', 'Ithaca Tompkins International Airport'), ('BPT', 'Jack Brooks Regional Airport (was Southeast Texas Regional)'), ('JAC', 'Jackson Hole Airport'), ('JAX', 'Jacksonville International Airport'), ('JAN', 'Jackson–Medgar Wiley Evers International Airport'), ('DAY', 'James M. Cox Dayton International Airport'), ('JMS', 'Jamestown Regional Airport'), ('JFK', 'John F. Kennedy International Airport (was New York International Airport)'), ('CMH', 'John Glenn Columbus International Airport'), ('SNA', 'John Wayne Airport (was Orange County Airport)'), ('JLN', 'Joplin Regional Airport'), ('NRR', 'José Aponte de la Torre Airport'), ('JNU', 'Juneau International Airport'), ('OGG', 'Kahului Airport'), ('AZO', 'Kalamazoo/Battle Creek International Airport'), ('MCI', 'Kansas City International Airport (originally Mid-Continent International Airport)'), ('ENA', 'Kenai Municipal Airport'), ('KTN', 'Ketchikan International Airport'), ('EYW', 'Key West International Airport'), ('GRK', 'Killeen–Fort Hood Regional Airport / Robert Gray Army Airfield'), ('BFI', 'King County International Airport (Boeing Field)'), ('AKN', 'King Salmon Airport'), ('KLW', 'Klawock Airport (also see Klawock Seaplane Base)'), ('RKD', 'Knox County Regional Airport'), ('ADQ', 'Kodiak Airport (Benny Benson State Airport)'), ('LSE', 'La Crosse Regional Airport'), ('LGA', 'LaGuardia Airport (and Marine Air Terminal)'), ('LFT', 'Lafayette Regional Airport'), ('LCH', 'Lake Charles Regional Airport'), ('MGM', 'Montgomery Regional Airport (Dannelly Field)'), ('LNY', 'Lanai Airport'), ('LAR', 'Laramie Regional Airport'), ('LRD', 'Laredo International Airport'), ('IFP', 'Laughlin/Bullhead International Airport'), ('LAW', 'Lawton–Fort Sill Regional Airport'), ('HOB', 'Lea County Regional Airport'), ('LEB', 'Lebanon Municipal Airport'), ('ABE', 'Lehigh Valley International Airport (was Allentown–Bethlehem–Easton International Airport)'), ('LWS', 'Lewiston–Nez Perce County Airport'), ('LIH', 'Lihue Airport'), ('LNK', 'Lincoln Airport (was Lincoln Municipal)'), ('LGB', 'Long Beach Airport (Daugherty Field)'), ('ISP', 'Long Island MacArthur Airport'), ('LAX', 'Los Angeles International Airport'), ('MSY', 'Louis Armstrong New Orleans International Airport'), ('SDF', 'Louisville International Airport (Standiford Field)'), ('LBB', 'Lubbock Preston Smith International Airport'), ('SJU', 'Luis Muñoz Marín International Airport'), ('LYH', 'Lynchburg Regional Airport (Preston Glenn Field)'), ('MBS', 'MBS International Airport'), ('TWF', 'Magic Valley Regional Airport (Joslin Field)'), ('MMH', 'Mammoth Yosemite Airport'), ('MHT', 'Manchester–Boston Regional Airport'), ('MHK', 'Manhattan Regional Airport'), ('MVY', "Martha's Vineyard Airport"), ('MFE', 'McAllen Miller International Airport'), ('LAS', 'McCarran International Airport'), ('TYS', 'McGhee Tyson Airport'), ('BFL', 'Meadows Field'), ('MLB', 'Melbourne Orlando International Airport'), ('MEM', 'Memphis International Airport'), ('PSE', 'Mercedita International Airport'), ('MEI', 'Meridian Regional Airport (Key Field)'), ('CDV', 'Merle K. (Mudhole) Smith Airport'), ('MRI', 'Merrill Field'), ('MIA', 'Miami International Airport'), ('BLV', 'MidAmerica St. Louis Airport / Scott Air Force Base'), ('MAF', 'Midland International Air and Space Port'), ('MKE', 'Milwaukee Mitchell International Airport'), ('MSP', 'Minneapolis–St. Paul International Airport (Wold–Chamberlain Field)'), ('MOT', 'Minot International Airport'), ('MSO', 'Missoula Montana Airport'), ('MOB', 'Mobile Regional Airport'), ('MKK', 'Molokai Airport (Hoolehua Airport)'), ('MLU', 'Monroe Regional Airport'), ('MRY', 'Monterey Regional Airport (was Monterey Peninsula Airport)'), ('MTJ', 'Montrose Regional Airport'), ('MKG', 'Muskegon County Airport'), ('MYR', 'Myrtle Beach International Airport'), ('ACK', 'Nantucket Memorial Airport'), ('BNA', 'Nashville International Airport (Berry Field)'), ('EWR', 'Newark Liberty International Airport'), ('PHF', 'Newport News/Williamsburg International Airport (Patrick Henry Field)'), ('IAG', 'Niagara Falls International Airport'), ('OME', 'Nome Airport'), ('ORF', 'Norfolk International Airport'), ('SJC', 'Norman Y. Mineta San José International Airport'), ('CKB', 'North Central West Virginia Airport (was Harrison-Marion Regional)'), ('LBF', 'North Platte Regional Airport (Lee Bird Field)'), ('XNA', 'Northwest Arkansas National Airport'), ('ECP', 'Northwest Florida Beaches International Airport[nb 2]'), ('OAK', 'Oakland International Airport'), ('OGD', 'Ogden-Hinckley Airport'), ('OGS', 'Ogdensburg International Airport'), ('ONT', 'Ontario International Airport'), ('ESD', 'Orcas Island Airport'), ('MCO', 'Orlando International Airport'), ('SFB', 'Orlando Sanford International Airport'), ('PGA', 'Page Municipal Airport'), ('PPG', 'Pago Pago International Airport'), ('PBI', 'Palm Beach International Airport'), ('PSP', 'Palm Springs International Airport'), ('EAT', 'Pangborn Memorial Airport'), ('PLN', 'Pellston Regional Airport'), ('PNS', 'Pensacola International Airport'), ('PSG', 'Petersburg James A. Johnson Airport'), ('PHL', 'Philadelphia International Airport'), ('PHX', 'Phoenix Sky Harbor International Airport'), ('AZA', 'Phoenix–Mesa Gateway Airport (formerly Williams AFB)'), ('GSO', 'Piedmont Triad International Airport'), ('PIR', 'Pierre Regional Airport'), ('PIT', 'Pittsburgh International Airport'), ('PGV', 'Pitt–Greenville Airport'), ('PBG', 'Plattsburgh International Airport'), ('PIH', 'Pocatello Regional Airport'), ('PDX', 'Portland International Airport'), ('PWM', 'Portland International Jetport'), ('PSM', 'Portsmouth International Airport at Pease'), ('PRC', 'Prescott Municipal Airport (Ernest A. Love Field)'), ('PVC', 'Provincetown Municipal Airport'), ('PVU', 'Provo Municipal Airport'), ('PUW', 'Pullman–Moscow Regional Airport'), ('PGD', 'Punta Gorda Airport'), ('MLI', 'Quad City International Airport'), ('BQN', 'Rafael Hernández International Airport'), ('RDU', 'Raleigh–Durham International Airport'), ('OTZ', 'Ralph Wien Memorial Airport'), ('HIB', 'Range Regional Airport (was Chisholm–Hibbing Airport)'), ('RAP', 'Rapid City Regional Airport'), ('RDD', 'Redding Municipal Airport'), ('RDM', 'Redmond Municipal Airport (Roberts Field)'), ('RNO', 'Reno/Tahoe International Airport'), ('RHI', 'Rhinelander–Oneida County Airport'), ('PVD', 'Rhode Island T. F. Green International Airport'), ('RIC', 'Richmond International Airport (Byrd Field)'), ('AMA', 'Rick Husband Amarillo International Airport'), ('LCK', 'Rickenbacker International Airport'), ('ROA', 'Roanoke–Blacksburg Regional Airport (Woodrum Field)'), ('RST', 'Rochester International Airport'), ('MFR', 'Rogue Valley International–Medford Airport'), ('DCA', 'Ronald Reagan Washington National Airport'), ('ROW', 'Roswell International Air Center'), ('ROP', 'Rota International Airport'), ('SMF', 'Sacramento International Airport'), ('SPN', 'Saipan International Airport (Francisco C. Ada)'), ('SLN', 'Salina Regional Airport'), ('SBY', 'Salisbury–Ocean City–Wicomico Regional Airport'), ('SLC', 'Salt Lake City International Airport'), ('SJT', 'San Angelo Regional Airport (Mathis Field)'), ('SAT', 'San Antonio International Airport'), ('SAN', 'San Diego International Airport (Lindbergh Field)'), ('SFO', 'San Francisco International Airport'), ('SBP', 'San Luis Obispo County Regional Airport (McChesney Field)'), ('SBA', 'Santa Barbara Municipal Airport (Santa Barbara Airport)'), ('SAF', 'Santa Fe Regional Airport'), ('SMX', 'Santa Maria Public Airport (Capt G. Allan Hancock Field)'), ('SRQ', 'Sarasota–Bradenton International Airport'), ('SAV', 'Savannah/Hilton Head International Airport'), ('MQT', 'Sawyer International Airport'), ('SEA', 'Seattle–Tacoma International Airport'), ('SHD', 'Shenandoah Valley Regional Airport'), ('SHR', 'Sheridan County Airport'), ('SHV', 'Shreveport Regional Airport'), ('SDY', 'Sidney–Richland Municipal Airport'), ('FSD', 'Sioux Falls Regional Airport (Joe Foss Field)'), ('SUX', 'Sioux Gateway Airport (Brig. General Bud Day Field)'), ('SIT', 'Sitka Rocky Gutierrez Airport'), ('SBN', 'South Bend International Airport'), ('RSW', 'Southwest Florida International Airport'), ('ABY', 'Southwest Georgia Regional Airport'), ('OTH', 'Southwest Oregon Regional Airport (was North Bend Municipal)'), ('RKS', 'Southwest Wyoming Regional Airport (Rock Springs–Sweetwater County Airport)'), ('GEG', 'Spokane International Airport (Geiger Field)'), ('SGF', 'Springfield–Branson National Airport'), ('STC', 'St. Cloud Regional Airport'), ('SGU', 'St. George Regional Airport (opened 2011)'), ('STL', 'St. Louis Lambert International Airport'), ('KSM', "St. Mary's Airport"), ('PIE', 'St. Pete–Clearwater International Airport'), ('SWF', 'Stewart International Airport'), ('SWO', 'Stillwater Regional Airport'), ('SCK', 'Stockton Metropolitan Airport'), ('SYR', 'Syracuse Hancock International Airport'), ('TLH', 'Tallahassee International Airport'), ('TPA', 'Tampa International Airport'), ('ANC', 'Ted Stevens Anchorage International Airport'), ('TXK', 'Texarkana Regional Airport (Webb Field)'), ('CID', 'The Eastern Iowa Airport'), ('TIQ', 'Tinian International Airport (West Tinian)'), ('TOL', 'Toledo Express Airport'), ('TTN', 'Trenton Mercer Airport'), ('PSC', 'Tri-Cities Airport'), ('TRI', 'Tri-Cities Regional Airport (Tri-Cities Regional TN/VA)'), ('HTS', 'Tri-State Airport (Milton J. Ferguson Field)'), ('TUS', 'Tucson International Airport'), ('TUL', 'Tulsa International Airport'), ('TUP', 'Tupelo Regional Airport (C.D. Lemons Field)'), ('HVN', 'Tweed-New Haven Airport'), ('TYR', 'Tyler Pounds Regional Airport'), ('UNK', 'Unalakleet Airport'), ('DUT', 'Unalaska Airport (Tom Madsen/Dutch Harbor Airport)'), ('SCE', 'University Park Airport'), ('CMI', 'University of Illinois - Willard Airport'), ('VDZ', 'Valdez Airport (Pioneer Field)'), ('VLD', 'Valdosta Regional Airport'), ('HRL', 'Valley International Airport'), ('VEL', 'Vernal Regional Airport (was Vernal-Uintah Co. Airport)'), ('ACT', 'Waco Regional Airport'), ('ALW', 'Walla Walla Regional Airport'), ('IAD', 'Washington Dulles International Airport'), ('ART', 'Watertown International Airport'), ('ATY', 'Watertown Regional Airport'), ('HPN', 'Westchester County Airport'), ('WST', 'Westerly State Airport'), ('BFF', 'Western Nebraska Regional Airport (William B. Heilig Field)'), ('ICT', 'Wichita Dwight D. Eisenhower National Airport (was Wichita Mid-Continent Airport)'), ('SPS', 'Wichita Falls Regional Airport / Sheppard Air Force Base'), ('BRW', 'Wiley Post–Will Rogers Memorial Airport'), ('AVP', 'Wilkes-Barre/Scranton International Airport'), ('OKC', 'Will Rogers World Airport'), ('HOU', 'William P. Hobby Airport'), ('IPT', 'Williamsport Regional Airport'), ('XWA', 'Williston Basin International Airport'), ('ILM', 'Wilmington International Airport'), ('ORH', 'Worcester Regional Airport'), ('WRG', 'Wrangell Airport (also see Wrangell Seaplane Base)'), ('YKM', 'Yakima Air Terminal (McAllister Field)'), ('YAK', 'Yakutat Airport (also see Yakutat Seaplane Base)'), ('HDN', 'Yampa Valley Airport (Yampa Valley Regional)'), ('CRW', 'Yeager Airport'), ('WYS', 'Yellowstone Airport'), ('COD', 'Yellowstone Regional Airport'), ('YUM', 'Yuma International Airport / MCAS Yuma')], max_length=3)),
            ],
        ),
    ]
