from ldap3 import Server, Connection, ALL
import json

class DukeLdap(object):

    #establish a connection to duke ldap
    def connection(self):
        server = Server('ldap.duke.edu', port=636, use_ssl=True)
        return Connection(server)


    def search(self):
        conn = self.connection()
        attributes=["uid","cn", "title", "eduPersonPrimaryAffiliation","eduPersonPrincipalName", "duDirJobDesc","mail","telephonenumber","givenname","cn","sn","displayname","edupersonaffiliation","duDukeId"]

        conn.bind()
        conn.search('dc=duke,dc=edu', '(uid=da129)',attributes=attributes)
        result = conn.entries
        conn.unbind()

        return json.loads(result[0].entry_to_json())



