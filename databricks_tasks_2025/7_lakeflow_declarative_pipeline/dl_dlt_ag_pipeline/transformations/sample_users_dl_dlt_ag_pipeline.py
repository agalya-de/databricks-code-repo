from pyspark import pipelines as dp

@dp.table()#4.store the final result into the table in the name of the function
def shipments1():#1.create a function
    df=spark.read.table("prodcatalog_wd36.logistics_wd36.bronze_shipments1")#2.write any pyspark program
    return df#3. return the final result