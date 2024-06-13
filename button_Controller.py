import pdf_generator
import db_manager
import clientes


def gerarQuote_Action (origin, language, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
                       companycity, paymenterm, freight, totalamount):

    #Função 1 = Armazenar Valores no Banco

    db_manager.inserir_quote(origin, language, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
                           companycity, paymenterm, freight, totalamount)

    # Função 2 = Gerar PDF

    pdf_generator.PDF_Generator(origin, language, currency, date, accountmanager, companyname, contactname, companytype, companycountry, companystate,
                              companycity, paymenterm, freight, totalamount)


def buttonCustomer ():
    clientes.ClientesJanela()