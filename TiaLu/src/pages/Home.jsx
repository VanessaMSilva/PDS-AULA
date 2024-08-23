import Menu from "./Menu";
import tia from '../assets/tialu.png'; // ajuste o caminho conforme a estrutura do seu projeto


function Home(){
    return(
        <div className="cut">
            <Menu/>
            <div className="supre">
                <div className="blocos">
                    <img src={tia} alt="" />
                </div>
                <div className="blocos">
                    <h1>Seja <br/> Bem-vindo(a)<br/>à Tia Lu</h1>
                    <h2>Farpas & Vendas</h2>
                    <button>Cadastrar funcionario</button>
                </div>
                
                
            </div>
        </div>
       
    )
}

export default Home