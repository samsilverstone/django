import json
import csv
import psycopg2

conn=psycopg2.connect(dbname="geolocation",user="nyaix",password="mclarenf1!@#")
cur=conn.cursor()

with open('/home/nyaixengn-x/Downloads/pincodes.txt','r') as json_file:
    data=json.load(json_file)
    x=data['India']
    for i in range(len(x)):
        func=lambda x: "'" + x[0:] + "'"
        officename=func(x[i]['officeName'])
        taluk=func(x[i]['taluk'])
        districtname=func(x[i]['districtName'])
        statename=func(x[i]['stateName'])
        cur.execute('''Insert into test("officename","pincode","taluk","districtname","statename") Values ({},{},{},{},{})'''.format(officename,x[i]['pincode'],taluk,districtname,statename))
    print("Values Entered Successfully")
    print("Committing to the db")
    conn.commit()
    print("Committing Successfull, closing Connection")

with open('/home/nyaixengn-x/Downloads/all-india-pincode-html-csv.csv','r') as csv_file:
    csv_reader=csv.DictReader(csv_file)
    count=0
    for row in csv_reader:
        func=lambda x:"'"+x.replace("'","''")+"'" if "'" in x else "'"+x[0:]+"'"
        officename=func(row['officename'])
        divisionname=func(row['divisionname'])
        regionname=func(row['regionname'])
        circlename=func(row['circlename'])
        taluk=func(row['Taluk'])
        districtname=func(row['Districtname'])
        statename=func(row['statename'])
        resuboffice=func(row['RelatedSuboffice'])
        reheadoffice=func(row['RelatedHeadoffice'])
        cur.execute('''Insert into pincodes("officename","pincode","divisionname",
        "regionname","circlename","taluk","districtname","statename","resuboffc",
        "reheadoffc") values ({},{},{},{},{},{},{},{},{},{})'''.format(officename,row['pincode'],divisionname,regionname,circlename,taluk,districtname,statename,resuboffice,reheadoffice))
        print(count)
        count=count+1    
    print("Values Entered Successfully")
    print("Committing to the db")
    conn.commit()
    print("Committing Successfull, closing Connection")

cur.execute('Select distinct statename from pincodes')
x=cur.fetchall()
for i in range(len(x)-1):
    func=lambda x: "'"+x+"'"
    value=func(x[i][0])
    print(i+1,value)
    cur.execute('Insert into states("state") values ({})'.format(value))
print("Inserted values Successfully,Committing values")
conn.commit()
print("commit Successfull,Closing Connection")

cur.execute('select distinct a.districtname,b.id from pincodes a inner join states b on a.statename=b.state')
x=cur.fetchall()
for i in range(len(x)):
    func=lambda y:"'"+y[0:]+"'"
    district=func(x[i][0])
    cur.execute('Insert into district("district","statename_id") values ({},{})'.format(district,x[i][1]))
print("Inserted values Successfully,Committing values")
conn.commit()
print("commit Successfull,Closing Connection")

cur.execute('select a.officename,a.pincode,a.divisionname,a.regionname,a.circlename,a.taluk,a.resuboffc,a.reheadoffc,b.id from pincodes a inner join district b on a.districtname=b.district')
x=cur.fetchall()
for i in range(len(x)):
    func=lambda x:"'"+x.replace("'","''")+"'" if "'" in x else "'"+x[0:]+"'"
    officename=func(x[i][0])
    divisionname=func(x[i][2])  
    regionname=func(x[i][3])
    circlename=func(x[i][4])
    taluk=func(x[i][5])
    resuboffice=func(x[i][6])
    reheadoffice=func(x[i][7])
    cur.execute('''Insert into pincode("officename","pincode","divisionname","regionname","circlename",
                    "taluk","resuboffc","reheadoffc","district_id") 
                    values ({},{},{},{},{},{},{},{},{})'''.format(officename,x[i][1],divisionname,regionname,circlename,taluk,resuboffice,reheadoffice,x[i][8]))
print("Inserted values Successfully,Committing values")
conn.commit()
print("commit Successfull,Closing Connection")



conn.close()



