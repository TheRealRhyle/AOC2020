valid = 0
countvalid = 0
invalidcount = 0
fields = ["byr", "iyr", "eyr","hgt", "hcl", "ecl" , "pid"]
pptbatch = []

with open ('day4data.txt') as file:
    idbatch = file.read()

id_batch = []
for line in idbatch.split("\n"):
    if not line:
        id_batch.append("~")
        continue
    id_batch.append(line)
    join_file = " ".join(id_batch)

batch = join_file.split('~ ')

for ppt in batch:
    pptfield = {}
    valid = []
    # pptbatch.append(ppt.strip())
    for passport in ppt.strip().split(" "):
        pptfield[passport.split(":")[0]] = passport.split(":")[1]
    
    #Validate fields
    try:
        valid.append(int(pptfield["byr"]) >= 1920 and int(pptfield["byr"]) <= 2002)
        valid.append(int(pptfield["iyr"]) >= 2010 and int(pptfield["iyr"]) <= 2020)
        valid.append(int(pptfield["eyr"]) >= 2020 and int(pptfield["eyr"]) <= 2030)
        # valid.append(pptfield["hgt"])
        if 'cm' in pptfield['hgt']:
            valid.append(int(pptfield['hgt'].strip("cm")) >= 150 and int(pptfield['hgt'].strip("cm")) <= 193)
        elif 'in' in pptfield['hgt']:
            valid.append(int(pptfield['hgt'].strip("in")) >= 59 and int(pptfield['hgt'].strip("in")) <= 76)
        else:
            valid.append(False)
        valid.append(len(pptfield["hcl"]) == 7 and "#" in pptfield["hcl"])
        valid.append(pptfield["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"])
        valid.append(len(pptfield["pid"]) == 9)
    except:
        valid.append(False)

    if all(valid):
        countvalid += 1
    else:
        invalidcount += 1

print(countvalid)


    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)
