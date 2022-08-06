#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pole
import re
import urllib2
import os

conexao = pole.http.Conexao('www.receita.fazenda.gov.br')
dados = conexao.obter_dados('/aplicacoes/atcta/cpf/ConsultaPublica.asp')
html = dados['conteúdo']
view = urllib2.quote(re.sub(".*<input type=hidden id=viewstate"
                            " name=viewstate value='([^']+)'.*", r'\1',
                            html, flags=re.DOTALL), '')
img_src = re.sub(".*<img border='0' id='imgcaptcha'"
                  " alt='Imagem com os caracteres anti rob.'"
                  " src='([^']+)'.*", r'\1', html,
                  flags=re.DOTALL).replace('&amp;', '&')
dados = conexao.obter_dados(img_src)
open('/tmp/captcha.jpg', 'wb').write(dados['conteúdo'])
os.system('xdg-open /tmp/captcha.jpg')
captcha = raw_input('Captcha: ')
cpf = raw_input('CPF: ')
inputs = ("txtCPF=%s&captcha=%s&captchaAudio=&viewstate=%s&"
           "Enviar=Consultar") % (cpf, captcha, view)
dados = conexao.obter_dados('/aplicacoes/atcta/cpf/'
                             'ConsultaPublicaExibir.asp', inputs)
html = dados['conteúdo']
nome = re.sub(".*Nome da Pessoa F.sica: ([^<]*).*", r'\1',
               html, flags=re.DOTALL).strip()
situacao = re.sub(".*Situa..o Cadastral: ([^<]*).*", r'\1',
                   html, flags=re.DOTALL).strip()
print "Nome:", nome
print "Situação:", situacao