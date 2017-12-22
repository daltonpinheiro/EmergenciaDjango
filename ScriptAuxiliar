#Serve para preencher o banco de dados rapidamente
require(sqldf)
db <- dbConnect(SQLite(), dbname="C:/Users/dalton.pinheiro/Documents/manchester/web/db.sqlite3")
dbListTables(db) 
 dbListFields(db, "formulario_dimdiscriminador"  )

tabela<- read.table("clipboard",sep="\t")
tabela<-data.frame(id=c(1:nrow(tabela)),DescDiscriminador=tabela$V1)
View(tabela)



dbWriteTable(conn = db, name = "formulario_dimdiscriminador", 
value = tabela, row.names = FALSE,append=T)


tabela<- read.table("clipboard",sep="\t")
tabela<-data.frame(id=c(1:nrow(tabela)),DescFluxograma=tabela$V1)
View(tabela)
dbListFields(db, "formulario_dimfluxograma" )
dbWriteTable(conn = db, name = "formulario_dimfluxograma", 
value = tabela, row.names = FALSE,append=T)



tab<-"formulario_dimclassificador"
 dbListFields(db, tab  )


tabela<- read.table("clipboard",sep="\t")
tabela<-data.frame(id=c(1:nrow(tabela)),DescClassificador=tabela$V1)
View(tabela)
dbWriteTable(conn = db, name = tab, 
value = tabela, row.names = FALSE,append=T)







tab<-"formulario_dimespecialidade" 
 dbListFields(db, tab  )


tabela<- read.table("clipboard",sep="\t")
tabela<-data.frame(id=c(1:nrow(tabela)),DescEspecialidade=tabela$V1)
View(tabela)
dbWriteTable(conn = db, name = tab, 
value = tabela, row.names = FALSE,append=T)










tab<-"formulario_dimprocedencia" 
 dbListFields(db, tab  )


tabela<- read.table("clipboard",sep="\t")
tabela<-data.frame(id=c(1:nrow(tabela)),DescProcedencia=tabela$V1)
View(tabela)
dbWriteTable(conn = db, name = tab, 
value = tabela, row.names = FALSE,append=T)







tab<-"formulario_dimchegada" 
 dbListFields(db, tab  )


tabela<- read.table("clipboard",sep="\t")
tabela<-data.frame(id=c(1:nrow(tabela)),DescChegada=tabela$V1)
View(tabela)
dbWriteTable(conn = db, name = tab, 
value = tabela, row.names = FALSE,append=T)







dbDisconnect(db)


