import Menu from "./../Menu";
import tia from './../../assets/tialu.png'; // ajuste o caminho conforme a estrutura do seu projeto


function Alterar(){
    return(
        <div>
            <Menu/>
        <div className="supre"></div>
        <div className="blocos">
        <div className="crud" id="center">
            <nav>
                <ul>
                    <li><a href="/Cadastrarp">Cadastrar</a></li>
                    <li><a href="/Alterarp">Alterar</a></li>
                    <li><a href="/Excluirp">Excluir</a></li>
                </ul>
            </nav>
        </div>
        <div className="forms">
            <form action="">
                <div>
                    <label htmlFor="Nome">Nome Produto:</label>
                    <input type="text" />
                </div>
                <div>
                    <label htmlFor="Nome">Codigo de barra:</label>
                    <input type="text" />
                </div>
                <div>
                    <label htmlFor="Nome">Tamanho:</label>
                    <input type="text" />
                </div>
                <div>
                    <label htmlFor="Nome">Informações:</label>
                    <input type="text" />
                </div>
                <div>
                    <label htmlFor="Nome">Imagem</label>
                    <input type="text" />
                </div>
                
                
                
                <button className="Alterar">Alterar</button>
            </form>
        </div>
    </div>
    <div className="blocos">
        <img src={tia} alt="" />
    </div>
    
    </div>
       
    )
}

export default Alterar