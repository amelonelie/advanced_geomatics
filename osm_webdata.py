import requests
from pyqgis_scripting_ext.core import *

place = "Merano"
url_string = "https://nominatim.openstreetmap.org/search?"
url_string += f"q={place}"
url_string += "&format=geojson"
url_string += "&polygon_geojson=1"
url_string += "&limit=1"


data= {'type': 'FeatureCollection', 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. http://osm.org/copyright', 'features': [{'type': 'Feature', 'properties': {'place_id': 61386684, 'osm_type': 'relation', 'osm_id': 47283, 'place_rank': 16, 'category': 'boundary', 'type': 'administrative', 'importance': 0.5606045519980116, 'addresstype': 'town', 'name': 'Meran - Merano', 'display_name': 'Meran - Merano, Burggrafenamt - Burgraviato, Bolzano - Bozen, Trentino-Alto Adige/Südtirol, 39012, Italia'}, 'bbox': [11.1364291, 46.6168347, 11.2397148, 46.6944533], 'geometry': {'type': 'Polygon', 'coordinates': [[[11.1364291, 46.6896835], [11.1365582, 46.6891861], [11.1365987, 46.6891764], [11.136653, 46.6888334], [11.1367995, 46.6883401], [11.1370608, 46.6883533], [11.1373184, 46.6883574], [11.1373865, 46.6883022], [11.1375451, 46.6879707], [11.137594, 46.6878843], [11.1375429, 46.6877503], [11.1375414, 46.6876918], [11.1376163, 46.6876004], [11.1377396, 46.6874946], [11.1378277, 46.6874075], [11.137723, 46.6872384], [11.1375452, 46.6869583], [11.1374521, 46.6867755], [11.137397, 46.686682], [11.1373358, 46.6865212], [11.1372161, 46.6861994], [11.1371682, 46.6860203], [11.1371352, 46.6859715], [11.1371059, 46.685954], [11.1369855, 46.6858755], [11.1369515, 46.6858534], [11.1368418, 46.6857655], [11.1367378, 46.6856369], [11.1367077, 46.685579], [11.1368064, 46.6854691], [11.1372132, 46.68534], [11.1376602, 46.6851922], [11.1381169, 46.6850622], [11.1386187, 46.6848953], [11.1394006, 46.6846197], [11.1402213, 46.6842713], [11.1404287, 46.6843079], [11.1406518, 46.6843263], [11.1409921, 46.6842929], [11.1409861, 46.6842619], [11.1409653, 46.6841539], [11.1409279, 46.6840331], [11.1409034, 46.6839301], [11.1408996, 46.6838132], [11.140939, 46.6835694], [11.1409687, 46.6834339], [11.1410337, 46.6832572], [11.1410716, 46.683162], [11.1411358, 46.6830708], [11.1412065, 46.6829974], [11.1412645, 46.6829559], [11.1413533, 46.6828867], [11.1414426, 46.682849], [11.1416692, 46.6827728], [11.1417747, 46.6827528], [11.1418678, 46.682723], [11.1418835, 46.6826518], [11.1418023, 46.6824193], [11.1422178, 46.6823845], [11.1425002, 46.6823747], [11.1427308, 46.6823569], [11.1428996, 46.6823268], [11.1431478, 46.6822591], [11.1433435, 46.6822464], [11.1435365, 46.6822293], [11.1436535, 46.6821911], [11.1437844, 46.6821122], [11.1438379, 46.6820663], [11.143865, 46.6820432], [11.1439452, 46.6818797], [11.1440478, 46.6817473], [11.1441026, 46.6817057], [11.1444201, 46.6816548], [11.145031, 46.6816028], [11.145152, 46.6815826], [11.1452174, 46.6815737], [11.145578, 46.681525], [11.1456162, 46.6815199], [11.1458189, 46.6814801], [11.1461072, 46.6814342], [11.1464353, 46.6813605], [11.1469002, 46.6813158], [11.1469387, 46.6812971], [11.1469473, 46.6811844], [11.1470625, 46.6811822], [11.1470624, 46.6811197], [11.1470029, 46.6811024], [11.1470687, 46.6808851], [11.1471262, 46.6806456], [11.1472443, 46.6802654], [11.1473464, 46.680016], [11.1474563, 46.6798204], [11.1475467, 46.6796252], [11.1475945, 46.6794713], [11.1476984, 46.6791859], [11.1477114, 46.6791364], [11.1477531, 46.6789779], [11.1477427, 46.6787947], [11.1477651, 46.6785996], [11.1476452, 46.67864], [11.1475667, 46.6786664], [11.1473805, 46.6787329], [11.1472549, 46.6787802], [11.1471408, 46.6788094], [11.1469911, 46.6788257], [11.1468732, 46.6788189], [11.1468198, 46.6787929], [11.146768, 46.6787581], [11.146735, 46.678736], [11.1465484, 46.678645], [11.146078, 46.6787168], [11.1453695, 46.6788606], [11.1451933, 46.6788909], [11.145089, 46.6787567], [11.1449667, 46.6786006], [11.1447902, 46.6783319], [11.1447088, 46.678252], [11.144598, 46.6780561], [11.1444191, 46.6781], [11.1443272, 46.6780144], [11.1442946, 46.6778638], [11.1443564, 46.6778356], [11.1442032, 46.6776162], [11.1440512, 46.6774544], [11.1440197, 46.677401], [11.1439428, 46.6772764], [11.1439242, 46.6772183], [11.1439151, 46.6771554], [11.1439202, 46.6770564], [11.1439603, 46.6769746], [11.1439083, 46.6768991], [11.1438884, 46.6768737], [11.1437034, 46.6766374], [11.1434651, 46.6763359], [11.1434436, 46.6763093], [11.1434357, 46.6762735], [11.143447, 46.6762283], [11.1434602, 46.6761695], [11.143491, 46.6761014], [11.1436972, 46.6759221], [11.1440239, 46.6756505], [11.1445905, 46.6752034], [11.1453274, 46.6746001], [11.1456398, 46.6743263], [11.1453987, 46.6742522], [11.145066, 46.674128], [11.1446321, 46.6739606], [11.1444561, 46.6738921], [11.1445281, 46.6738224], [11.1448906, 46.6735457], [11.1445473, 46.6733036], [11.1446241, 46.6732261], [11.1447201, 46.6731257], [11.1447825, 46.672984], [11.1447897, 46.6728917], [11.1448425, 46.6728901], [11.1454139, 46.6725326], [11.1443097, 46.6717652], [11.1441705, 46.6716694], [11.1444974, 46.6714996], [11.1451652, 46.6710574], [11.1457015, 46.6707367], [11.1459763, 46.670604], [11.1467984, 46.6701671], [11.146652, 46.6698324], [11.1464521, 46.6695707], [11.1464022, 46.6695396], [11.1463607, 46.6695139], [11.1455445, 46.6692457], [11.1453806, 46.6691723], [11.1450434, 46.6689311], [11.144858, 46.6688086], [11.1447771, 46.6687425], [11.1446491, 46.6686505], [11.1445101, 46.6685046], [11.1443586, 46.6683725], [11.1440472, 46.6681848], [11.1434782, 46.6678445], [11.1431482, 46.6676237], [11.1424939, 46.6680385], [11.1422933, 46.6682132], [11.1419111, 46.6685083], [11.1411303, 46.6691574], [11.1407775, 46.6689095], [11.140474, 46.6686972], [11.1401963, 46.6684928], [11.139975, 46.6683511], [11.1397832, 46.6681908], [11.1395567, 46.6680214], [11.1393907, 46.6679046], [11.1393553, 46.6678797], [11.138985, 46.6676137], [11.1389612, 46.6675916], [11.1391549, 46.667282], [11.1396485, 46.6669533], [11.1399796, 46.6667716], [11.1403029, 46.6666215], [11.1404894, 46.666501], [11.1407136, 46.6663664], [11.140872, 46.6662374], [11.1410462, 46.6660991], [11.1413454, 46.665936], [11.1416095, 46.6657961], [11.1416882, 46.6657406], [11.1417483, 46.6656495], [11.1419055, 46.6653271], [11.141987, 46.6651366], [11.1419928, 46.6649115], [11.1419769, 46.6647138], [11.1419498, 46.6645658], [11.1421166, 46.6643422], [11.1422586, 46.664173], [11.1424874, 46.6639662], [11.1426755, 46.6638277], [11.1428414, 46.6637661], [11.1430004, 46.6636956], [11.1431238, 46.6635943], [11.1432082, 46.6635162], [11.1432049, 46.6633723], [11.1431482, 46.6630539], [11.143125, 46.6628672], [11.1430537, 46.6622952], [11.1430258, 46.6620437], [11.1430308, 46.6619851], [11.1433475, 46.6615471], [11.1434081, 46.6614651], [11.1438788, 46.6607048], [11.1442796, 46.6601798], [11.1444738, 46.6599054], [11.1445056, 46.6598606], [11.1447552, 46.6595004], [11.144945, 46.6591774], [11.1450551, 46.6589053], [11.1451401, 46.6586787], [11.1451552, 46.6585029], [11.1452292, 46.6583486], [11.145328, 46.6582027], [11.1455729, 46.6578876], [11.1458624, 46.6575447], [11.1460521, 46.6573432], [11.1463865, 46.6570219], [11.1466576, 46.6567693], [11.1470492, 46.656447], [11.1474478, 46.6561155], [11.1483561, 46.655455], [11.1488127, 46.6551044], [11.1492267, 46.6547681], [11.1498414, 46.6542841], [11.1505621, 46.6537351], [11.1506633, 46.6536536], [11.1508897, 46.6534679], [11.1514824, 46.6529663], [11.1518252, 46.6527124], [11.1524154, 46.6522693], [11.153135, 46.6516932], [11.1539192, 46.651098], [11.1544658, 46.6506692], [11.1551157, 46.650189], [11.1556474, 46.6497965], [11.1560682, 46.6494736], [11.1565368, 46.6491182], [11.1575476, 46.6483882], [11.1583045, 46.6478294], [11.159303, 46.6470996], [11.1602825, 46.6463656], [11.161499, 46.6454742], [11.162295, 46.6448922], [11.1631273, 46.6443004], [11.1639141, 46.6437141], [11.1647434, 46.6431089], [11.1653593, 46.6426608], [11.1656453, 46.6424393], [11.1661902, 46.642015], [11.1668202, 46.6415531], [11.1676085, 46.6409847], [11.1681076, 46.6405793], [11.1684795, 46.6403022], [11.1687493, 46.6400631], [11.1690558, 46.6397648], [11.1692454, 46.6395632], [11.1694178, 46.6393619], [11.1695553, 46.6392063], [11.1696182, 46.6391242], [11.1696947, 46.6390777], [11.1698409, 46.6389759], [11.1702101, 46.6387529], [11.1704748, 46.6385949], [11.1705993, 46.6385206], [11.1710307, 46.6382604], [11.1714952, 46.6379501], [11.1719451, 46.6376592], [11.1720732, 46.6375669], [11.1721061, 46.6375425], [11.172317, 46.637426], [11.1724381, 46.637114], [11.1727004, 46.6364377], [11.173, 46.6356375], [11.173224, 46.6350553], [11.1734013, 46.634548], [11.173577, 46.6340881], [11.1737367, 46.6336866], [11.1736986, 46.6336729], [11.1733441, 46.6335454], [11.1734372, 46.6334082], [11.1736743, 46.6330601], [11.1741684, 46.6323517], [11.174349, 46.6320993], [11.1746212, 46.6317293], [11.1751974, 46.6309134], [11.1758869, 46.6299531], [11.1764145, 46.6292239], [11.1768233, 46.6286419], [11.1772349, 46.6280413], [11.1777653, 46.6272517], [11.1781676, 46.6266395], [11.1785651, 46.6260298], [11.1789356, 46.62546], [11.179248, 46.6249691], [11.1796138, 46.6243781], [11.1801349, 46.6235904], [11.1804585, 46.6231362], [11.1810526, 46.6222862], [11.1812013, 46.6220305], [11.1815549, 46.621476], [11.1817673, 46.6211419], [11.1818954, 46.6209357], [11.1819534, 46.620775], [11.1820691, 46.6205341], [11.1823897, 46.6197027], [11.1842403, 46.6201056], [11.1847318, 46.620216], [11.1852929, 46.6203734], [11.1868196, 46.6207259], [11.1870748, 46.6207797], [11.1881854, 46.6210136], [11.1892685, 46.6211937], [11.1916556, 46.6218639], [11.1918093, 46.621989], [11.1929639, 46.6222697], [11.1935906, 46.6224662], [11.1941288, 46.6225762], [11.1953038, 46.6223727], [11.1960088, 46.6223119], [11.1964346, 46.6224054], [11.1973712, 46.62252], [11.1978582, 46.6226019], [11.1990095, 46.6227376], [11.1995476, 46.6227236], [11.2001402, 46.6226066], [11.2011484, 46.6224966], [11.2016388, 46.6222931], [11.2022349, 46.6220756], [11.2029978, 46.6221107], [11.2029832, 46.6218362], [11.2030445, 46.6215275], [11.203116, 46.6213473], [11.2032148, 46.6211508], [11.2033169, 46.6209894], [11.2034021, 46.6206643], [11.2035111, 46.6204959], [11.2026664, 46.6204116], [11.2023565, 46.6198479], [11.2022304, 46.6195531], [11.2021828, 46.6193402], [11.2021555, 46.6189121], [11.2023701, 46.6187835], [11.2027856, 46.6184139], [11.2028503, 46.618346], [11.2028912, 46.6182805], [11.2029457, 46.618215], [11.203024, 46.6181635], [11.2031058, 46.6180255], [11.2031977, 46.6179273], [11.2032965, 46.6178337], [11.2034259, 46.6176816], [11.2036746, 46.6175787], [11.2037767, 46.6174758], [11.2039368, 46.6173892], [11.2046623, 46.6170032], [11.204826, 46.616973], [11.2055347, 46.6168347], [11.2053508, 46.6169563], [11.2053126, 46.6172732], [11.2052328, 46.6175448], [11.2054861, 46.617857], [11.205493, 46.618529], [11.2055243, 46.618815], [11.2055728, 46.6190294], [11.2058851, 46.6198158], [11.2061245, 46.6201946], [11.2055936, 46.6201446], [11.2051981, 46.6200826], [11.2047333, 46.6199945], [11.2044765, 46.6199778], [11.2042649, 46.6202066], [11.2040255, 46.6205973], [11.2042996, 46.6207332], [11.204369, 46.6217482], [11.2042822, 46.6218531], [11.2044488, 46.622301], [11.2042108, 46.6225099], [11.2041259, 46.6226558], [11.2040975, 46.6227125], [11.2040291, 46.6229427], [11.2039728, 46.6233262], [11.2039347, 46.6235635], [11.2038615, 46.6237759], [11.2038214, 46.6238942], [11.2037695, 46.6240028], [11.2037577, 46.6241519], [11.203668, 46.6244502], [11.2035995, 46.6248052], [11.2035028, 46.6251634], [11.2033187, 46.6257664], [11.2032006, 46.6261214], [11.2031228, 46.6264018], [11.2030095, 46.626585], [11.2028749, 46.6269448], [11.2028301, 46.6270177], [11.2025563, 46.6272917], [11.2023982, 46.627504], [11.2023274, 46.6276985], [11.2022164, 46.6277261], [11.2021763, 46.6277698], [11.2020819, 46.6280162], [11.2020866, 46.6280762], [11.2021149, 46.6281361], [11.2022188, 46.6282772], [11.2024336, 46.6285738], [11.2027711, 46.6291459], [11.2030331, 46.6295511], [11.2046711, 46.6297943], [11.205686, 46.6298947], [11.2060613, 46.6299596], [11.206826, 46.6300617], [11.2070714, 46.6301589], [11.2072957, 46.6303016], [11.2081833, 46.6305353], [11.2088454, 46.6306698], [11.2089138, 46.6307792], [11.2095237, 46.6314188], [11.2099359, 46.6318864], [11.2106085, 46.6322508], [11.2098608, 46.6325992], [11.2092066, 46.6329167], [11.2090714, 46.6333728], [11.2089228, 46.6337773], [11.2091281, 46.6339882], [11.2093668, 46.6342059], [11.2104432, 46.634662], [11.2111367, 46.634945], [11.2113111, 46.6350182], [11.2114961, 46.6351091], [11.2115835, 46.6351704], [11.2117523, 46.6353651], [11.2120173, 46.6357155], [11.2123586, 46.6361949], [11.2127924, 46.63674], [11.2124992, 46.6370201], [11.2124794, 46.637556], [11.2118634, 46.6379099], [11.211884, 46.638094], [11.2117425, 46.6381687], [11.2117634, 46.6384608], [11.2111481, 46.6391342], [11.2101908, 46.6401697], [11.2102109, 46.6402381], [11.2102814, 46.6404694], [11.2095869, 46.6411038], [11.2087376, 46.6419257], [11.2072961, 46.641985], [11.2071373, 46.6420376], [11.2069551, 46.6420546], [11.2066307, 46.6421103], [11.2063916, 46.6421555], [11.2062285, 46.6421811], [11.2059774, 46.6422129], [11.2057281, 46.6422268], [11.2055166, 46.6422488], [11.2053666, 46.6422562], [11.2052201, 46.642268], [11.2050776, 46.6422573], [11.2049213, 46.6422288], [11.204738, 46.6421603], [11.2045462, 46.642083], [11.2042789, 46.6420162], [11.2043888, 46.6422301], [11.2044557, 46.6424493], [11.2045851, 46.6427798], [11.2047219, 46.6431101], [11.204902, 46.6435026], [11.2050885, 46.643913], [11.2052756, 46.6443369], [11.205404, 46.6446224], [11.2054804, 46.6448324], [11.2055125, 46.6451198], [11.2055604, 46.6455149], [11.2056162, 46.6459233], [11.2056844, 46.6462955], [11.2057344, 46.646641], [11.2057367, 46.6469379], [11.2060396, 46.6471751], [11.2061322, 46.6472633], [11.2062082, 46.6474463], [11.2063506, 46.6475336], [11.2065451, 46.6476558], [11.2066325, 46.6477576], [11.2067376, 46.6479311], [11.2068247, 46.6481634], [11.2068792, 46.6483001], [11.206912, 46.6483822], [11.2068989, 46.6485219], [11.2068558, 46.6487509], [11.2067836, 46.6491226], [11.2066999, 46.6494123], [11.2067033, 46.6494977], [11.2066851, 46.6496915], [11.2066772, 46.6498987], [11.2066036, 46.6502781], [11.2065566, 46.650468], [11.2065943, 46.6506922], [11.2066706, 46.6509023], [11.2067849, 46.6512015], [11.2068005, 46.6513227], [11.2067447, 46.6514768], [11.2067426, 46.6516074], [11.2067147, 46.6518644], [11.2066492, 46.6521806], [11.2066193, 46.6523297], [11.2066379, 46.6524058], [11.2065816, 46.6526094], [11.206679, 46.652774], [11.2072941, 46.6526137], [11.2084368, 46.6524521], [11.2082828, 46.6529411], [11.2082109, 46.6532035], [11.2081222, 46.6535517], [11.2080522, 46.6538995], [11.2080012, 46.654112], [11.2079746, 46.654261], [11.2079643, 46.6544277], [11.2079506, 46.6545134], [11.2079555, 46.6545943], [11.2079756, 46.6547064], [11.2079859, 46.6548592], [11.2079887, 46.6549267], [11.2081559, 46.6550224], [11.2083046, 46.6551231], [11.2085442, 46.6552489], [11.2087782, 46.6553794], [11.2090173, 46.6555323], [11.2092303, 46.6555687], [11.2095258, 46.6556035], [11.2098342, 46.6556335], [11.2098997, 46.6556772], [11.2099337, 46.6558296], [11.2099631, 46.6559685], [11.2100007, 46.6561703], [11.2100194, 46.6562284], [11.2101699, 46.6564325], [11.2101967, 46.6564905], [11.2103922, 46.6566352], [11.2111548, 46.6572279], [11.2112773, 46.6573066], [11.21141, 46.6574165], [11.2114415, 46.6574879], [11.2117235, 46.6579909], [11.2116769, 46.6584103], [11.2116151, 46.65892], [11.2118351, 46.6594062], [11.2120696, 46.6600271], [11.2122109, 46.6603664], [11.2122948, 46.6605808], [11.2123993, 46.6608397], [11.2124777, 46.6610587], [11.2126343, 46.6611322], [11.2131508, 46.6608972], [11.2137513, 46.6606381], [11.2138917, 46.6606353], [11.2138476, 46.6607757], [11.2138321, 46.6609155], [11.2138506, 46.6609871], [11.2139121, 46.6610534], [11.2140124, 46.66111], [11.2141155, 46.661153], [11.2142279, 46.6611643], [11.2145424, 46.6611852], [11.2147506, 46.6611812], [11.2151918, 46.6617216], [11.2154266, 46.6620501], [11.215541, 46.6621694], [11.2162768, 46.6619031], [11.2166992, 46.6624619], [11.2170075, 46.6628294], [11.2173581, 46.6626921], [11.2174745, 46.6626809], [11.2175711, 46.662706], [11.2180937, 46.6629388], [11.2185149, 46.6631287], [11.2187858, 46.6632404], [11.2190788, 46.6632122], [11.2196471, 46.6624857], [11.2200126, 46.662039], [11.2203763, 46.6621386], [11.2204614, 46.6621819], [11.220563, 46.6621889], [11.2207586, 46.6621581], [11.2209655, 46.6621226], [11.2215711, 46.6620479], [11.2219699, 46.6619906], [11.2223916, 46.6619329], [11.2227988, 46.661862], [11.223704, 46.6615834], [11.2240389, 46.6617209], [11.2246537, 46.6624874], [11.2250123, 46.6628854], [11.2252304, 46.6630432], [11.2256146, 46.6634452], [11.2259298, 46.6637991], [11.2265082, 46.6641163], [11.2270874, 46.664015], [11.2277246, 46.6638946], [11.2281461, 46.6638144], [11.228465, 46.6643572], [11.2289047, 46.6650956], [11.2299359, 46.664819], [11.230241, 46.6647275], [11.2303831, 46.6647472], [11.230481, 46.6650603], [11.2303229, 46.6658059], [11.2306535, 46.6663934], [11.2308353, 46.6664034], [11.2312234, 46.6663238], [11.2315539, 46.6662364], [11.2321222, 46.6660678], [11.2324687, 46.6659305], [11.2331419, 46.6660074], [11.2335102, 46.6664997], [11.233697, 46.667027], [11.2336467, 46.6673925], [11.2336299, 46.6674603], [11.2334762, 46.6679358], [11.2337589, 46.6679752], [11.2343489, 46.6680762], [11.2347736, 46.6681894], [11.2350742, 46.668485], [11.2354686, 46.6679643], [11.2356577, 46.6678931], [11.2361047, 46.6676369], [11.2364359, 46.6674864], [11.2368583, 46.6673657], [11.2370514, 46.6676094], [11.2374923, 46.6679593], [11.2375776, 46.6680266], [11.2378376, 46.6684445], [11.2380647, 46.6688405], [11.2381499, 46.6690638], [11.2381771, 46.6692478], [11.23817, 46.6694909], [11.2381492, 46.6698963], [11.2380856, 46.6704151], [11.2384869, 46.6707717], [11.23893, 46.6710735], [11.2391466, 46.6711953], [11.2394804, 46.6715217], [11.2396634, 46.6716576], [11.2396197, 46.672302], [11.2396581, 46.6729132], [11.2396702, 46.6734844], [11.2396, 46.6740393], [11.2395731, 46.6747733], [11.2396193, 46.6753573], [11.2396475, 46.6758203], [11.2397148, 46.6760665], [11.2394265, 46.6762071], [11.2390305, 46.6765118], [11.2388564, 46.6766502], [11.2376399, 46.6770745], [11.2370821, 46.676865], [11.2369414, 46.6767417], [11.2367313, 46.6765433], [11.236321, 46.6761059], [11.2360443, 46.6756973], [11.2356518, 46.6753765], [11.2359054, 46.6749665], [11.2358204, 46.6748467], [11.2353283, 46.6743478], [11.2348354, 46.6740065], [11.2342506, 46.6734194], [11.2339696, 46.672669], [11.2315969, 46.6730933], [11.2315582, 46.673067], [11.2313946, 46.6730027], [11.2312096, 46.6729748], [11.2310568, 46.6729553], [11.2308848, 46.6729452], [11.2307384, 46.6729615], [11.2305673, 46.6729739], [11.2304475, 46.6729627], [11.2303353, 46.6729379], [11.2302179, 46.6728637], [11.2301332, 46.6728113], [11.2300545, 46.6727049], [11.2300064, 46.6726293], [11.2299428, 46.672572], [11.2298587, 46.6725557], [11.2297588, 46.6725891], [11.2296308, 46.6726771], [11.2295384, 46.6727149], [11.2294377, 46.6727484], [11.229286, 46.6727558], [11.2290822, 46.6727283], [11.2288965, 46.6726824], [11.2286839, 46.6726011], [11.228328, 46.6724505], [11.2281398, 46.6724047], [11.227897, 46.6723824], [11.2276832, 46.6723506], [11.2275107, 46.672309], [11.2273121, 46.6722273], [11.22714, 46.6721767], [11.2270482, 46.6721695], [11.2269239, 46.6721854], [11.2268274, 46.6722053], [11.2267628, 46.6722425], [11.2267214, 46.6722883], [11.2266788, 46.6723657], [11.2266786, 46.6724602], [11.2267441, 46.6725624], [11.2268125, 46.6726375], [11.2269075, 46.6727212], [11.2269848, 46.6727737], [11.2270023, 46.6728228], [11.2270116, 46.6728677], [11.2269932, 46.6729175], [11.2269476, 46.6729814], [11.2266463, 46.6730683], [11.2264295, 46.67314], [11.226342, 46.6731777], [11.2262557, 46.6732469], [11.2262024, 46.6733019], [11.226138, 46.6733256], [11.2260684, 46.6733345], [11.2259513, 46.6733158], [11.2257174, 46.6732708], [11.2250612, 46.6732116], [11.2247987, 46.6731852], [11.2246616, 46.6731699], [11.2245183, 46.6731232], [11.2243333, 46.6730368], [11.2238654, 46.6728254], [11.2236981, 46.6727296], [11.2235398, 46.6726967], [11.2233557, 46.6726913], [11.2232628, 46.6726571], [11.223143, 46.6726054], [11.2226561, 46.6727274], [11.2224815, 46.6727938], [11.222374, 46.6728229], [11.2222437, 46.6728344], [11.2219522, 46.6727996], [11.2213155, 46.6726769], [11.221237, 46.672656], [11.2211298, 46.6725906], [11.2210269, 46.6724936], [11.2209353, 46.6723918], [11.2208054, 46.6723314], [11.2204117, 46.6722175], [11.220292, 46.6721658], [11.2202086, 46.672145], [11.2200533, 46.6721255], [11.2198783, 46.6720614], [11.2197587, 46.6720142], [11.2196608, 46.6719981], [11.2194415, 46.6719709], [11.2192418, 46.6719432], [11.2190595, 46.6719018], [11.2189063, 46.6718507], [11.2187186, 46.6717374], [11.2186221, 46.6717168], [11.2184084, 46.6716669], [11.218212, 46.6715987], [11.2179605, 46.6715046], [11.2178469, 46.6714438], [11.2177059, 46.671352], [11.2175265, 46.6712025], [11.2174516, 46.671168], [11.2171888, 46.6711956], [11.2170318, 46.6711941], [11.2168944, 46.6711698], [11.2167682, 46.6711407], [11.2166499, 46.671107], [11.2165478, 46.6710865], [11.2164009, 46.6711119], [11.2162645, 46.6711325], [11.2155098, 46.6711201], [11.2151169, 46.6711052], [11.2149697, 46.6711216], [11.2148902, 46.6711366], [11.2147697, 46.671166], [11.2146595, 46.6712086], [11.2145205, 46.6712653], [11.2142212, 46.6714016], [11.2138605, 46.671593], [11.2137735, 46.6716442], [11.213677, 46.6716821], [11.2135691, 46.6717202], [11.2134383, 46.6717587], [11.2133617, 46.6717647], [11.2132608, 46.6717531], [11.2131192, 46.6717289], [11.2129644, 46.6717004], [11.2127745, 46.6716321], [11.2126125, 46.6715677], [11.2123934, 46.6715629], [11.2121003, 46.6716091], [11.2117585, 46.6716652], [11.2114777, 46.6716977], [11.2114305, 46.6717072], [11.2113736, 46.6717132], [11.2112817, 46.6717149], [11.2109913, 46.671707], [11.2108651, 46.671678], [11.2104572, 46.6715329], [11.209958, 46.671376], [11.2097919, 46.6713297], [11.2096824, 46.6713094], [11.2093722, 46.6712974], [11.2090787, 46.671312], [11.2090678, 46.6711457], [11.208978, 46.671089], [11.2085462, 46.6708993], [11.2084237, 46.6708792], [11.2081258, 46.6708489], [11.2078271, 46.6708367], [11.2075585, 46.6708239], [11.2073013, 46.6708289], [11.2067345, 46.6708758], [11.2059545, 46.6709403], [11.2052293, 46.6709543], [11.2052, 46.6710764], [11.2050945, 46.6711144], [11.2049525, 46.6712207], [11.2047921, 46.6713542], [11.2045841, 46.6714842], [11.2042685, 46.6716613], [11.2040446, 46.6717601], [11.2038603, 46.6717907], [11.203568, 46.6717963], [11.2032171, 46.6717671], [11.2029146, 46.6717234], [11.2026964, 46.6717231], [11.2023897, 46.671756], [11.2018415, 46.6717171], [11.2017141, 46.671841], [11.2014831, 46.672048], [11.2011908, 46.6723146], [11.2007528, 46.6725975], [11.2006171, 46.6726361], [11.2001121, 46.6728168], [11.1998951, 46.672866], [11.1999188, 46.6729465], [11.199735, 46.6730086], [11.1995701, 46.6729712], [11.1993684, 46.6729346], [11.1992325, 46.6729687], [11.1990015, 46.6730767], [11.1988465, 46.6731021], [11.1986884, 46.6730917], [11.1985451, 46.6730044], [11.1984044, 46.6729217], [11.198219, 46.6729027], [11.197906, 46.6728817], [11.1973897, 46.6728647], [11.1969073, 46.6729189], [11.196212, 46.6728603], [11.1957045, 46.6728385], [11.19558, 46.6729534], [11.1950068, 46.6727214], [11.1944344, 46.6724894], [11.1939161, 46.6725849], [11.1936115, 46.6725097], [11.1933438, 46.6724158], [11.1930602, 46.6722953], [11.1928793, 46.6722268], [11.1926923, 46.6721898], [11.1924451, 46.6721586], [11.192225, 46.6721718], [11.1918716, 46.6722011], [11.1916257, 46.6722234], [11.1910588, 46.6722077], [11.1905733, 46.672226], [11.190231, 46.6722685], [11.19, 46.6720868], [11.1898512, 46.6719698], [11.1896899, 46.6720404], [11.1895742, 46.6720696], [11.1891467, 46.6715198], [11.1890988, 46.6714667], [11.1889643, 46.6713748], [11.1885687, 46.6712168], [11.1878486, 46.6714276], [11.1875619, 46.6715321], [11.1873708, 46.6715943], [11.1872419, 46.6716192], [11.1870419, 46.6716456], [11.1867321, 46.6716386], [11.1860235, 46.671557], [11.1857166, 46.6716484], [11.185484, 46.6720803], [11.1852951, 46.6724619], [11.1850859, 46.6729474], [11.1849489, 46.6732785], [11.1846144, 46.6739194], [11.1845298, 46.6741325], [11.1844649, 46.6742462], [11.1848291, 46.6743608], [11.1850479, 46.6744376], [11.1851974, 46.6745787], [11.1852544, 46.6746136], [11.1853837, 46.6746786], [11.1857336, 46.6749869], [11.1856514, 46.6750988], [11.185676, 46.6751185], [11.1859087, 46.6752761], [11.1859691, 46.6752929], [11.1860105, 46.6753686], [11.1856871, 46.6755548], [11.1855985, 46.675507], [11.1850606, 46.6758053], [11.1850212, 46.6758825], [11.1852019, 46.6759871], [11.1850004, 46.6761455], [11.184756, 46.6763376], [11.1847204, 46.6763877], [11.1844298, 46.6768613], [11.1848062, 46.6775426], [11.184746, 46.6777327], [11.1844309, 46.6780042], [11.1842706, 46.6781423], [11.1839667, 46.6782876], [11.1835501, 46.678435], [11.183556, 46.6785384], [11.1835946, 46.6786862], [11.1836419, 46.6788247], [11.1836423, 46.6789372], [11.1836762, 46.6790266], [11.1837887, 46.6792044], [11.1838168, 46.6792714], [11.1838463, 46.6794553], [11.1838642, 46.679698], [11.1838843, 46.6798101], [11.1839219, 46.6799129], [11.1839832, 46.6799927], [11.1840508, 46.6800499], [11.1841049, 46.6800939], [11.1841243, 46.6801295], [11.1841097, 46.6802738], [11.1840483, 46.6803109], [11.1839682, 46.680371], [11.183784, 46.6803835], [11.1837772, 46.6804601], [11.183641, 46.6805257], [11.1835186, 46.6805325], [11.1834039, 46.6805257], [11.1833416, 46.6804999], [11.1833384, 46.6803785], [11.183012, 46.6804522], [11.1830119, 46.6805512], [11.1829079, 46.6805667], [11.1827875, 46.6806005], [11.1826388, 46.6806843], [11.1824575, 46.6808498], [11.1823476, 46.6809824], [11.182188, 46.6811789], [11.1821112, 46.6813424], [11.1820352, 46.6815238], [11.1819727, 46.681696], [11.1819401, 46.6818406], [11.1819325, 46.6819982], [11.1819348, 46.6821557], [11.1819453, 46.682295], [11.1819565, 46.6824118], [11.1819908, 46.6825326], [11.1820439, 46.6826428], [11.1821104, 46.6827823], [11.1821703, 46.6828487], [11.1820913, 46.6829177], [11.1823238, 46.6830887], [11.1823439, 46.6833448], [11.1819519, 46.6834333], [11.1818826, 46.6835761], [11.1818372, 46.6836695], [11.181439, 46.6840101], [11.1810644, 46.6842872], [11.1810609, 46.6843233], [11.1816084, 46.6846458], [11.1815496, 46.6848899], [11.1815004, 46.6850484], [11.1814917, 46.6851565], [11.1814889, 46.6852691], [11.1814954, 46.6854309], [11.1814584, 46.6855486], [11.1813705, 46.6857393], [11.1812075, 46.6859134], [11.1811279, 46.6861084], [11.1810252, 46.6862994], [11.1809201, 46.6863053], [11.180839, 46.6863434], [11.1807897, 46.6864164], [11.1807541, 46.686507], [11.1807824, 46.686601], [11.1807957, 46.6866682], [11.1808536, 46.6867661], [11.1809323, 46.6868459], [11.1810153, 46.686925], [11.1809584, 46.6869441], [11.1807675, 46.6868803], [11.1805356, 46.6868262], [11.1803013, 46.6867722], [11.1800956, 46.6867176], [11.1799311, 46.6866937], [11.1798555, 46.6867042], [11.179741, 46.6867423], [11.1796208, 46.6867806], [11.1795293, 46.6867824], [11.1793662, 46.686772], [11.1792609, 46.686774], [11.1790829, 46.6867999], [11.1789366, 46.6868207], [11.1788513, 46.6868133], [11.1787585, 46.6868016], [11.1786414, 46.6868173], [11.178484, 46.6868653], [11.1782889, 46.6868735], [11.1780525, 46.6868465], [11.1778181, 46.6868105], [11.1771217, 46.6867292], [11.1771155, 46.6864324], [11.1771443, 46.6859908], [11.1771736, 46.6855808], [11.1771917, 46.685117], [11.1771885, 46.6848377], [11.1771881, 46.684802], [11.1771851, 46.6844241], [11.1771435, 46.6841819], [11.1770675, 46.6838144], [11.1769548, 46.6834115], [11.1768907, 46.6830978], [11.1767949, 46.6828296], [11.1767376, 46.6826237], [11.1765882, 46.6823026], [11.176469, 46.6819584], [11.1763331, 46.6816685], [11.176137, 46.6813437], [11.1760275, 46.6811613], [11.1758267, 46.6808636], [11.1756309, 46.6805659], [11.1754802, 46.6803752], [11.1752989, 46.6801537], [11.1750232, 46.6798214], [11.1749, 46.6796551], [11.1747779, 46.6794931], [11.1746422, 46.6793292], [11.1744827, 46.6791613], [11.1742518, 46.6789271], [11.1739979, 46.6786485], [11.1737799, 46.6784096], [11.1735786, 46.6781795], [11.1734628, 46.6780017], [11.1733427, 46.67786], [11.173246, 46.6777313], [11.1731681, 46.6775618], [11.1730916, 46.6774058], [11.1730278, 46.677263], [11.1729839, 46.6771468], [11.1729678, 46.6769896], [11.1729471, 46.6767785], [11.1729359, 46.6766213], [11.1729501, 46.6763645], [11.1729699, 46.6761661], [11.1730178, 46.6759537], [11.1730678, 46.6758358], [11.1731533, 46.6756632], [11.17322, 46.6755539], [11.1734483, 46.6752571], [11.173594, 46.6750383], [11.1736645, 46.674902], [11.1737169, 46.674721], [11.1737202, 46.6745589], [11.1736912, 46.6743255], [11.1736057, 46.6741291], [11.1735719, 46.6739993], [11.1735082, 46.6739195], [11.1734335, 46.6738489], [11.1733482, 46.6737605], [11.1732641, 46.6736991], [11.1731307, 46.6736342], [11.1730311, 46.6735956], [11.1728797, 46.67357], [11.1727678, 46.6735511], [11.1726162, 46.6735405], [11.1724786, 46.6735116], [11.1719003, 46.6733829], [11.1717292, 46.6733703], [11.1716906, 46.6733675], [11.1716097, 46.6733616], [11.1714657, 46.6733778], [11.1713271, 46.6734479], [11.1708335, 46.6733043], [11.1702761, 46.6733824], [11.1701225, 46.6732818], [11.170042, 46.6732293], [11.1698986, 46.6731601], [11.169769, 46.6731265], [11.1696611, 46.6731061], [11.1694601, 46.6730649], [11.1692134, 46.6730246], [11.1691504, 46.6730033], [11.1691015, 46.6729457], [11.1689517, 46.672674], [11.1689273, 46.6726291], [11.1688257, 46.6725684], [11.1687763, 46.6723939], [11.1686903, 46.6722065], [11.1686611, 46.6721306], [11.168552, 46.6719976], [11.1684699, 46.6718642], [11.1684067, 46.6717349], [11.1684213, 46.6716086], [11.1683051, 46.6715434], [11.1682232, 46.671553], [11.1679679, 46.6717342], [11.1678664, 46.6718127], [11.1677572, 46.6718597], [11.1676414, 46.6719069], [11.1675376, 46.6719269], [11.1673767, 46.6719299], [11.1672441, 46.6719234], [11.1670418, 46.6718508], [11.1668633, 46.6718812], [11.1666426, 46.6718808], [11.1665161, 46.6719462], [11.166315, 46.672067], [11.1661622, 46.6721284], [11.1658006, 46.6722793], [11.165627, 46.6724761], [11.1655119, 46.6725412], [11.1654075, 46.6728312], [11.1648461, 46.6729948], [11.1647721, 46.6729422], [11.1646361, 46.6728098], [11.1644894, 46.6726776], [11.16427, 46.6724837], [11.1642383, 46.6724663], [11.1641597, 46.6724633], [11.1637282, 46.6726245], [11.1637051, 46.6727014], [11.1637043, 46.6727419], [11.1637073, 46.6728184], [11.163809, 46.6731403], [11.1637303, 46.6732094], [11.1637333, 46.6734704], [11.1636832, 46.6736063], [11.1636117, 46.6736977], [11.1635033, 46.6737672], [11.1633877, 46.6738189], [11.163262, 46.6738843], [11.1631329, 46.6739857], [11.1630405, 46.6741269], [11.1629928, 46.6744068], [11.1629601, 46.6746729], [11.1629515, 46.6750106], [11.1626818, 46.6750697], [11.1625377, 46.6751264], [11.1622425, 46.67551], [11.1620571, 46.6757385], [11.1619279, 46.6759389], [11.1618155, 46.6761345], [11.1616986, 46.6763572], [11.161647, 46.6764977], [11.1616094, 46.6766019], [11.1615964, 46.6767056], [11.1616006, 46.6767988], [11.1616044, 46.6768855], [11.1616181, 46.6770247], [11.1616262, 46.6771866], [11.1616844, 46.6773339], [11.1617786, 46.6775032], [11.1618966, 46.6775099], [11.1620166, 46.6775482], [11.1621949, 46.6776123], [11.1623215, 46.6776729], [11.1624791, 46.6777509], [11.1625175, 46.6777727], [11.1626822, 46.6778641], [11.1627669, 46.678083], [11.1628391, 46.6783561], [11.162905, 46.6786968], [11.1621595, 46.6786929], [11.1621896, 46.6791603], [11.1616091, 46.6794818], [11.1614049, 46.6796071], [11.1611696, 46.6796913], [11.1609175, 46.6797423], [11.160616, 46.6798065], [11.1603343, 46.6798524], [11.1602474, 46.6798675], [11.1602086, 46.6799177], [11.1600421, 46.6801909], [11.159809, 46.6805552], [11.159724, 46.6806379], [11.1594418, 46.6809987], [11.1592913, 46.6811815], [11.1591864, 46.6813185], [11.1591076, 46.681392], [11.1584554, 46.6816788], [11.1581393, 46.6818062], [11.1580745, 46.6818614], [11.1578837, 46.68218], [11.157761, 46.6823623], [11.1575137, 46.682493], [11.1573201, 46.6824561], [11.1572347, 46.6824668], [11.1570244, 46.6825202], [11.1568041, 46.6823669], [11.1567855, 46.6825967], [11.1566602, 46.6826306], [11.1565604, 46.682691], [11.1564119, 46.6828198], [11.1562342, 46.6828726], [11.1561291, 46.6828611], [11.1557493, 46.6830932], [11.1556473, 46.6831582], [11.1555586, 46.6832093], [11.1553567, 46.6832491], [11.1551879, 46.6832793], [11.1550072, 46.6832782], [11.1547885, 46.6835118], [11.1546281, 46.6837128], [11.1546485, 46.6838565], [11.1546416, 46.6839286], [11.154624, 46.6840009], [11.1546012, 46.6840643], [11.1545578, 46.6841236], [11.1545111, 46.684183], [11.1544428, 46.6842113], [11.1543603, 46.6842534], [11.1542619, 46.6842462], [11.1541688, 46.6842075], [11.1540786, 46.6842002], [11.1538927, 46.6841902], [11.1536446, 46.6841993], [11.1534736, 46.6842161], [11.1533828, 46.6842538], [11.1528434, 46.6839894], [11.1522207, 46.6842981], [11.1516083, 46.6845617], [11.1514839, 46.684618], [11.1514355, 46.6846549], [11.1513612, 46.6847598], [11.1512694, 46.684856], [11.1512158, 46.684947], [11.151173, 46.6848983], [11.1510396, 46.6847703], [11.1505696, 46.6844822], [11.1502942, 46.6842759], [11.1500007, 46.6841914], [11.1499684, 46.6841977], [11.1499144, 46.6842082], [11.1495767, 46.6845684], [11.1495212, 46.6845928], [11.1493367, 46.6846584], [11.1492396, 46.6847232], [11.1490991, 46.6848293], [11.1489483, 46.6849627], [11.1489267, 46.6850351], [11.1489173, 46.6851702], [11.1488016, 46.6852399], [11.1485379, 46.6854968], [11.1482709, 46.6857493], [11.1479698, 46.6860295], [11.147741, 46.6862411], [11.1476647, 46.6863952], [11.1475934, 46.686536], [11.1476973, 46.6865791], [11.147934, 46.6866736], [11.1481212, 46.6867781], [11.1482542, 46.6868746], [11.1481958, 46.6869477], [11.1480286, 46.6870588], [11.1478854, 46.6871785], [11.1477717, 46.6872392], [11.1477203, 46.6872557], [11.1476594, 46.6872728], [11.1475738, 46.6873194], [11.1474479, 46.6874207], [11.147313, 46.6874413], [11.147269, 46.6874646], [11.147033, 46.687739], [11.1469314, 46.6878759], [11.1467465, 46.6879964], [11.1465541, 46.6880783], [11.1464363, 46.6880589], [11.1463318, 46.6880717], [11.1460406, 46.6884371], [11.1461798, 46.688484], [11.1462344, 46.688645], [11.1462758, 46.6887612], [11.1463037, 46.6889091], [11.1463377, 46.689066], [11.1463508, 46.6892322], [11.1462283, 46.6892863], [11.146068, 46.6891701], [11.1459121, 46.6890515], [11.1457704, 46.6889416], [11.145576, 46.688796], [11.1453217, 46.6887979], [11.1452873, 46.6887977], [11.1448853, 46.6887681], [11.1447996, 46.6887619], [11.144725, 46.6887768], [11.1446911, 46.6889299], [11.144682, 46.6889711], [11.1446584, 46.6891605], [11.1446637, 46.6892729], [11.1446915, 46.6893354], [11.1447363, 46.689393], [11.1447934, 46.6894325], [11.1447965, 46.6895089], [11.1446765, 46.6895336], [11.1445838, 46.6895669], [11.1445071, 46.6896313], [11.1443692, 46.6897824], [11.1442653, 46.6899058], [11.1441335, 46.6899398], [11.1439347, 46.689957], [11.1438022, 46.6899955], [11.143603, 46.6900847], [11.1435835, 46.6901301], [11.1435707, 46.6902608], [11.1435528, 46.6903872], [11.1433489, 46.690481], [11.1430443, 46.6906127], [11.1426051, 46.6905849], [11.1423673, 46.6905039], [11.1421404, 46.6903805], [11.1420909, 46.6903561], [11.1419812, 46.6903311], [11.1418422, 46.6903112], [11.1416038, 46.6902977], [11.1413486, 46.6902935], [11.1412185, 46.6903094], [11.1412169, 46.6903402], [11.1412148, 46.6903815], [11.1412536, 46.6904752], [11.1413374, 46.6906717], [11.1414574, 46.6908944], [11.1415453, 46.6910503], [11.1416011, 46.6911392], [11.1416286, 46.6911927], [11.1416445, 46.6912644], [11.1416474, 46.6913993], [11.1416301, 46.6915616], [11.1416245, 46.6916877], [11.1416201, 46.6918048], [11.1416634, 46.6921145], [11.1417638, 46.6927291], [11.1418109, 46.6932187], [11.1418213, 46.693358], [11.1418549, 46.6934428], [11.1418804, 46.6935279], [11.1419137, 46.6935857], [11.1419636, 46.6936478], [11.142073, 46.6937268], [11.1421627, 46.6937836], [11.1422173, 46.693841], [11.1422641, 46.6939302], [11.1423056, 46.6940284], [11.1423714, 46.6941621], [11.1424231, 46.6942287], [11.142577, 46.6943383], [11.1426915, 46.6944216], [11.1426805, 46.6944533], [11.1424898, 46.6943444], [11.1422058, 46.6941922], [11.1417685, 46.6939439], [11.1414894, 46.6937917], [11.1412301, 46.693621], [11.1406709, 46.6934335], [11.1405231, 46.6933958], [11.1405105, 46.6933465], [11.1406778, 46.6930914], [11.1407509, 46.692955], [11.1407956, 46.6928867], [11.1408251, 46.6928052], [11.1408317, 46.6926835], [11.1408144, 46.6925984], [11.1407771, 46.6924821], [11.1407232, 46.6923796], [11.1406487, 46.692273], [11.1404363, 46.69207], [11.1402646, 46.6919022], [11.1401279, 46.6917743], [11.1400569, 46.6916946], [11.1399781, 46.6916241], [11.1399274, 46.691562], [11.1398788, 46.6914909], [11.139859, 46.6914238], [11.1398491, 46.6912755], [11.139866, 46.6911447], [11.1397968, 46.690885], [11.1397211, 46.6906839], [11.1396855, 46.6904056], [11.1396507, 46.6903522], [11.1395986, 46.6903352], [11.1393838, 46.6902987], [11.1390403, 46.6902332], [11.1384875, 46.6901445], [11.1383058, 46.6901164], [11.1381587, 46.6900967], [11.1380437, 46.6901033], [11.1377939, 46.6901125], [11.1375407, 46.6900137], [11.1372572, 46.6899335], [11.1364291, 46.6896835]]]}}]}

if not data:
    response = requests.get(url_string)
    if response.status_code == 200:
        #everything went well
        data = response.json()
    else:
        # error
        print("Requests errored with code:", response.status_code)
        print(response.text)
else:
    print("using cached data")


coordinates = data["features"][0]["geometry"]["coordinates"][0]
boundingbox = data["features"][0]["bbox"]
polygon = HPolygon.fromCoords(coordinates)

crsHelper = HCrs()
crsHelper.from_srid(4326)
crsHelper.to_srid(3857)   

proj_poly = crsHelper.transform(polygon)


canvas = HMapCanvas.new()    
canvas.add_geometry(proj_poly)

osm = HMap.get_osm_layer()
canvas.set_layers([osm])


canvas.set_extent(proj_poly.bbox())
canvas.show()