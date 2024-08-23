import Menu from "./../Menu";
import tia from '../../assets/tialu.png'; // ajuste o caminho conforme a estrutura do seu projeto


function Excluir(){
    return(
        <div>
            <Menu/>
        <div className="supre"></div>
        <div className="blocos">
        <div className="crud" id="center">
            <nav>
                <ul>
                    <li><a href="/Cadastrarv">Cadastrar</a></li>
                    <li><a href="/Alterarv">Alterar</a></li>
                    <li><a href="/Excluirv">Excluir</a></li>
                </ul>
            </nav>
        </div>
        <div className="forms">
            <form action="" method="POST">
                <div>
                    <label htmlFor="CPF">CPF Cliente:</label>
                    <input type="text" />
                </div>                     

          
                <button className="Excluir">Excluir</button>

            </form>
        </div>
    </div>
    <div className="blocos">
        <img src={tia} alt="" />
    </div>
    
    </div>
       
    )
}

export default Excluir