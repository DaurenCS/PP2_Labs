
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]



def bool(name):
	for i in range(len(movies)):
		if name ==movies[i]["name"]:
			if movies[i]["imdb"] > 5.5:
				print('True')

def sublist():
	for i in range(len(movies)):
			if movies[i]["imdb"] > 5.5:
				print(movies[i])


def category(cat):
	for i in range(len(movies)):
		if cat ==movies[i]["category"]:
			print(movies[i]["name"])

def IMBD(list):	
	s = 0
	for i in movies:
		if i['name'] in list:
			s += i["imdb"]
	return s/len(list)

def IMBD_for_cat(cat):	
	s = 0
	n = 0
	for i in movies:
		if i['category'] == cat:
			s += i['imdb']
			n += 1
	return s/n




