import streamlit as st
from import_data import *
from graficos import *

st.title("🌐 Visão Geral")

st.markdown('''
### **Levantamento das Ações e Políticas Públicas na Prevenção e Enfrentamento da Violência contra Crianças e Adolescentes**

Com o objetivo de fortalecer a legislação que assegura e protege os direitos das crianças e adolescentes, especialmente aqueles expostos à violência, foi instituída a **Lei nº 13.431/2017**, regulamentada pelo **Decreto nº 9.603/2018**. 

Essa legislação organiza o **Sistema de Garantias de Direitos para Crianças e Adolescentes Vítimas ou Testemunhas de Violência (SGDCA)**, estabelecendo procedimentos que asseguram um atendimento especializado e integrado, prevenindo a **revitimização** e promovendo a **proteção integral**.

> **"Os filhos dos outros e os filhos de ninguém são nossa responsabilidade constitucional e moral."**  
> — *Pedro Hartung, Instituto Alana*
            
Nesta conjuntura, a avaliação e o monitoramento das políticas públicas relacionadas ao SGDCA na prevenção e enfrentamento da violência contra crianças e adolescentes não são apenas uma prerrogativa dos Tribunais de Contas, mas também um imperativo ético e social. 

A atenção dispensada a esta etapa vital da vida humana é determinante para moldar gerações mais saudáveis, instruídas e aptas a contribuir positivamente para a sociedade. 
Por meio da confluência de esforços institucionais, dados concretos e compromisso com a vida e o bem-estar infantil, as Cortes de Contas e a ATRICON reafirmam seu compromisso em não apenas identificar falhas e áreas de melhoria, mas também em ser catalisador de transformações significativas que ecoarão por décadas, fortalecendo o tecido social e garantindo um futuro mais promissor para as crianças de todo o Brasil. 

Destarte, com o intuito de verificar as ações e políticas públicas desenvolvidas pelos entes do SGDCA em diferentes estados do Brasil, na prevenção e enfrentamento da violência contra crianças e adolescentes, e em alinhamento à ação 27 do Plano Anual de Trabalho da Rede Integrar, a ATRICON desenvolveu o **PROJETO INFÂNCIA SEGURA**.

##### **Tribunais de Contas Partícipes**
''')

st.html('''
<table style="border-collapse: collapse; width: 100%; border: 1px solid #ccc; text-align: center;">
  <tr>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-PI</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-AM</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-CE</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-SC</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-RO</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-PB</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-MS</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-PR</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-RR</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-PE</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-MT</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-MG</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-PA</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-RN</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-GO</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-RJ</td>
  </tr>
  <tr>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-TO</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-BA</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-RS</td>
    <td style="border: 1px solid #ccc; padding: 8px;">TCE-ES</td>
  </tr>
</table>
''')

st.markdown('''         
---

### **A Realidade Atual: O Sistema que Falha**
Apesar da existência de normativos internacionais, nacionais, políticas e planos estaduais, os dados apontam para uma dura realidade:  
**Nosso sistema falha em proteger a infância e juventude.**

A principal conclusão do levantamento conduzido pela **ATRICON**, com a participação ativa de 20 tribunais de contas estaduais, é alarmante:  

### **A Criança e o Adolescente NÃO são a prioridade absoluta no Brasil.**

---

### **Principais Deficiências Identificadas**
1. **Falta de integração e coordenação entre os órgãos do SGDCA.**  
2. **Descontinuidade das políticas públicas relacionadas ao tema.**  
3. **Ausência de ciclos periódicos de avaliação e monitoramento.**  
4. **Recursos inadequados para a execução das políticas públicas.**  
5. **Inexistência de um sistema unificado e seguro para o compartilhamento de informações.**  
   - Isso torna a rede de proteção mais vulnerável a falhas de comunicação, duplicidade de informações e perda de dados essenciais para o acompanhamento dos casos.

#### **Consequências**  
- **11 estados** apresentam **alto risco de revitimização**.  
- **9 unidades da federação** possuem risco **médio**.

---

### **Benefícios do Levantamento**
Este levantamento gerou informações cruciais sobre as ações e políticas públicas desenvolvidas pelos entes do **SGDCA** na prevenção e enfrentamento da violência infantil. Os principais benefícios incluem:

- **Autoavaliação:** Ferramenta útil para gestores.
- **Mapeamento de riscos:** Para fiscalizações futuras.  
- **Controle externo e social:** Apoio aos órgãos de controle e à sociedade.  
- **Fortalecimento das estratégias de governança:**  
  - Implementação de fluxos de atendimento bem definidos.  
  - Aprimoramento da infraestrutura.  
  - Garantia de recursos orçamentários específicos.  

---

### **O Futuro que Precisamos Construir**
Para que as crianças e adolescentes sejam realmente tratados como prioridade absoluta, é essencial:  
- Garantir a precedência dos direitos em todas as esferas da sociedade e do poder público.  
- Implementar políticas públicas eficazes e coordenadas.  

---

📄 **Acesse o Relatório Completo:**  
''')

# Caminho para o arquivo PDF
file_path = "pdf/Levantamento_Infancia_Segura_Atricon.pdf"

# Ler o arquivo em modo binário
with open(file_path, "rb") as pdf_file:
    pdf_content = pdf_file.read()

# Criar o botão de download
st.download_button(
    label="🔗 Clique aqui para acessar o relatório completo.",
    data=pdf_content,  # Conteúdo do arquivo
    file_name="levantamento_infancia_segura_2024.pdf",  # Nome do arquivo para download
    mime="application/pdf"  # Tipo MIME do arquivo
)

st.markdown('''
---

Esta é uma oportunidade de refletirmos e agirmos para mudar a realidade das nossas crianças e adolescentes. A responsabilidade é de todos nós!
''')