import re
from modulo import*   

def achar_url(html, pagina_inicial, pagina_mae, urls_printadas, nivel):
    """Acha e imprime as urls válidas dentro da página HTML"""
    if html is None:  #esse é o final da recursão pois indica que não há nada no link
        pass
    else:
        href= {""}
        padrao = '(?<=href=["\']).+?(?=["\'])'
        urls = re.findall(padrao, html)
        for url in urls:
            url = resolver_url(url, pagina_mae)  
            if eh_url_valida(url,pagina_inicial):
                if url not in urls_printadas:     #certifica que essa url já não foi colocada na árvore
                    urls_printadas.append(url)
                    print(f"{nivel * '  '}{url}")
                    html = obter_html(url)
                    achar_url(html,pagina_inicial,url, urls_printadas, nivel + 1)
        
           
def main():
    pagina_inicial = input()
    html = obter_html(pagina_inicial)  #devolve um texto com o conteúdo do link
    urls_printadas = []    #lista que conterá todas as urls da árvore
    nivel = 0              #referente à hierarquia da url na árvore
    achar_url(html,pagina_inicial, pagina_inicial, urls_printadas,nivel)

main()    