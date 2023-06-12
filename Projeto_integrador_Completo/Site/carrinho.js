// ativar
let iconeCarrinho = document.querySelector("#carrinho_icone")
let carrinho = document.querySelector(".carrinho")


iconeCarrinho.onclick = () =>{
    carrinho.classList.toggle("ativar")
}
//


if(document.readyState == "loading"){
    document.addEventListener("DOMContentLoaded", ready) 
 }
else{
     ready();
 }



function ready(){
    var removerCarinhobtn = document.getElementsByClassName("carrinho_remover")
    console.log(removerCarinhobtn)
    for (var i = 0; i < removerCarinhobtn.length; i++){
        var botao = removerCarinhobtn[i]
        botao.addEventListener("click", removerCarinhoItem)
    }

    var quantiInput = document.getElementsByClassName("carrinho_quanti")
    for (var i = 0; i < quantiInput.length; i++){
        var input = quantiInput[i]
        input.addEventListener("change", quantiMudar)
    }

    var addCarrinho = document.getElementsByClassName("carrinho_btn")
    for (var i = 0; i < addCarrinho.length; i++){
        var botao = addCarrinho[i];
        botao.addEventListener("click", addCarrinhoClick);
    }

    document.getElementsByClassName("btn_comprar")[0].addEventListener("click", comprarClick)
}

// comprar
function comprarClick(){
    alert("Compra finalizada!")
    var carrinhoCont =  document.getElementsByClassName("container_carrinho")[0]
    while (carrinhoCont.hasChildNodes()){
        carrinhoCont.removeChild(carrinhoCont.firstChild)
    }
    contador = 0;
    atualizarTotal()
}

// Remover
function removerCarinhoItem(event){
    contador -= 1;
    var botaoClick = event.target
    botaoClick.parentElement.remove()
    atualizarTotal()
}
//

var contador = 0;

// Add carrinho
function addCarrinhoClick(event){
    var botao = event.target
    var produtos = botao.parentElement
    var nomeP = produtos.getElementsByClassName("nome")[0].innerText
    var valorP = produtos.getElementsByClassName("valor")[0].innerText
    
    var imgP = produtos.getElementsByClassName("p_img")[0].src
    if(contador < 5){
        addProdutoCarrinho(nomeP, valorP, imgP)
        atualizarTotal()
    }
    
    
   
}

function addProdutoCarrinho(nomeP, valorP, imgP){
    contador += 1;
    var carrinhoShopBox = document.createElement("div")
    carrinhoShopBox.classList.add("carrinho_box")
    var carrinhoItens = document.getElementsByClassName("container_carrinho")[0]
    var carrinhoItensNome = carrinhoItens.getElementsByClassName("carrinho_produto_nome")
    for( var i = 0; i < carrinhoItensNome.length; i++){
        if(carrinhoItensNome[i].innerText == nomeP){
           return; 
        }
        
    }
    var carrinhoBoxContainer = `
                <img src="${imgP}" alt="" class="carrinho_img">
                <div class="detalhe_box">
                    <div class="carrinho_produto_nome">${nomeP}</div>
                    <div class="carrinho_valor">${valorP}</div>
                    <input type="number" value="1" class="carrinho_quanti">
                </div>
                <!--Remover-->
                <i class="fa-solid fa-trash-arrow-up carrinho_remover" style="color: #dc143c;" ></i>
    `
    carrinhoShopBox.innerHTML = carrinhoBoxContainer
    carrinhoItens.append(carrinhoShopBox)
    carrinhoShopBox.getElementsByClassName("carrinho_remover")[0].addEventListener("click", removerCarinhoItem)
    carrinhoShopBox.getElementsByClassName("carrinho_quanti")[0].addEventListener("change", quantiMudar)
}

    



// Quantidade mudar
function quantiMudar(event){
    var input = event.target
    if(isNaN(input.value) || input.value <= 0){
        input.value = 1
    }
    atualizarTotal()
}

// total
function atualizarTotal(){
    var carrinhoCont = document.getElementsByClassName("container_carrinho")[0]
    var carrinhoBoxs = carrinhoCont.getElementsByClassName("carrinho_box")
    var total = 0;
    for (var i = 0; i < carrinhoBoxs.length; i++){
        var carrinhoBox = carrinhoBoxs[i]
        var valorElemento = carrinhoBox.getElementsByClassName("carrinho_valor")[0]
        var valor = parseFloat(valorElemento.innerText.replace("R$: ", ""))
        
        var valor = parseFloat(valorElemento.innerText.replace("R$: ", "").replace(".", "").replace(",", "."))
        var quantiElemento = carrinhoBox.getElementsByClassName("carrinho_quanti")[0]
        var quanti = quantiElemento.value
        total += (valor * quanti);
    }
       
        document.getElementsByClassName("total_valor")[0].innerText = "R$: " + total.toFixed(2);
    
}