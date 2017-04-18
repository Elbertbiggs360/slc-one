import pprint
from googleapiclient.discovery import build

def main():
	service = build("customsearch", "v1", developerkey="AIzaSyAe7X0thGuy55yogRTQ24wdqRLLD3qyLao")

	res = service.cse(
		q='andela',
		cx='countryCA').list(
	).execute()
	pprint.pprint(res)

if __name__ == '__main__':
	main()