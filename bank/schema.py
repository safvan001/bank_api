import graphene
from graphene_django import DjangoObjectType
from graphene import relay
from bank.models import Branch, Bank

class BanksType(DjangoObjectType):
    class Meta:
        model = Bank
        interfaces = (relay.Node, )

class BranchType(DjangoObjectType):
    class Meta:
        model = Branch
        interfaces = (relay.Node, )


class BankConnection(relay.Connection):
    class Meta:
        node = BanksType

class BranchConnection(relay.Connection):
    class Meta:
        node = BranchType


class Query(graphene.ObjectType):
    banks = graphene.ConnectionField(BankConnection)
    branches = graphene.ConnectionField(BranchConnection)

    def resolve_banks(self, info, **kwargs):
        return Bank.objects.all()
    
    def resolve_branches(self, info, **kwargs):
        return Branch.objects.select_related('bank').all()
    
schema = graphene.Schema(query=Query)






