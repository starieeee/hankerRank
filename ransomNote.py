from collections import Counter
def checkMagazine(magazine, note):
    mag = Counter(magazine)
    nte = Counter(note)
    result = nte - mag
    if result == {}:
        return "Yes"
    else:
        return "No"
def main():
    print(checkMagazine(['give', 'me', 'one', 'grand', 'today', 'night'], ['give', 'one', 'grand', 'today']))
main()