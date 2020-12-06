valid = 0
fields = ["byr", "iyr", "eyr","hgt", "hcl", "ecl" , "pid"]

    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)


with open ('day4data.txt') as sample:
    idbatch = sample.read()

id_batch = []
for line in idbatch.split("\n"):
    if not line:
        id_batch.append("~")
        continue
    id_batch.append(line)
    join_file = " ".join(id_batch)

for line in join_file.split("~ "):
    res = all(ele in line for ele in fields)
    if res:
        valid += 1

print(valid)

# print(join_file.replace("~", "\n"))