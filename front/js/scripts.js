/*
  --------------------------------------------------------------------------------------
  Função para limpar campos do formulário
  --------------------------------------------------------------------------------------
*/
function limparCamposForm() {
    document.getElementById("ccateg").value = '';
    document.getElementById("timesp").value = '';
    document.getElementById("nvideo").value = '';
    document.getElementById("nquizz").value = '';
    document.getElementById("qscore").value = '';
    document.getElementById("corate").value = '';
    document.getElementById("device").value = '';
    document.getElementById('resultado').style.display = 'none';
}


/*
  --------------------------------------------------------------------------------------
  Função para preparar o envio de uma solicitação de predição
  --------------------------------------------------------------------------------------
*/
const prepararPredicao = () => {
    let ccateg = document.getElementById("ccateg").value;
    let timesp = document.getElementById("timesp").value;
    let nvideo = document.getElementById("nvideo").value;
    let nquizz = document.getElementById("nquizz").value;
    let qscore = document.getElementById("qscore").value;
    let corate = document.getElementById("corate").value;
    let device = document.getElementById("device").value;

    if (ccateg.trim() !== "" && timesp.trim() !== "" && nvideo.trim() !== "" && nquizz.trim() !== "" &&
        qscore.trim() !== "" && corate.trim() !== "" && device.trim() !== "") {
        try {
            postPredicao(ccateg, timesp, nvideo, nquizz, qscore, corate, device);
        } catch (error) {
            alert("Ocorreu um erro e a predição não foi realizada!");
        }
    } else {
        alert("Por favor, preencha todos os campos antes de enviar.");
    }
}


/*
  --------------------------------------------------------------------------------------
  Função com a rota POST que realiza uma predição
  --------------------------------------------------------------------------------------
*/
const postPredicao = async (ccateg, timesp, nvideo, nquizz, qscore, corate, device) => {
    let formData = new FormData();
    formData.append('ccateg', ccateg);
    formData.append('timesp', timesp);
    formData.append('nvideo', nvideo);
    formData.append('nquizz', nquizz); 
    formData.append('qscore', qscore);  
    formData.append('corate', corate); 
    formData.append('device', device);  
 
    let url = 'http://127.0.0.1:5000/predicao';
    fetch(url, {
        method: 'post',
        body: formData
    })
        .then((response) => response.json())
        .then((data) => {
            exibirResultado(data.predicao);
        })
        .catch((error) => {
        console.error('Error:', error);
    });
}


/*
  --------------------------------------------------------------------------------------
  Função para exibir o resultado da solicitação de predição
  --------------------------------------------------------------------------------------
*/
const exibirResultado = (predicao) => {
    const resultadoTexto = document.getElementById('resultado-texto');
    if (predicao === 0) {
        resultadoTexto.textContent = "NÃO CONCLUI O CURSO!";
        resultadoTexto.className = "resultado-negativo";
    } else if (predicao === 1) {
        resultadoTexto.textContent = "CONCLUI O CURSO!";
        resultadoTexto.className = "resultado-positivo";
    } else {
        resultadoTexto.textContent = "Resultado desconhecido";
        resultadoTexto.className = "";
    }
    document.getElementById('resultado').style.display = 'block'; // Torna a div visível
}


/*
  --------------------------------------------------------------------------------------
  Função para ocultar o resultado anterior ao realizar uma nova consulta
  --------------------------------------------------------------------------------------
*/
const ocultarResultado = () => {
    document.getElementById('resultado').style.display = 'none';
}


/*
  --------------------------------------------------------------------------------------
  Chamada dos Tooltips do Bootstrap para dados de exemplo
  --------------------------------------------------------------------------------------
*/
document.addEventListener('DOMContentLoaded', function () {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl)
    })
});
