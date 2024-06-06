from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Scripts:

    def __init__(self, drive: webdriver, wait: WebDriverWait):

        self.drive = drive
        self.wait = wait

    def pesquisar_js(self, index_ano: int,
                     index_municipio: int,
                     index_entidade: int):

        functions = """
    function getAllOptionValues(selectlist, select_target, 
                                 index_target, send=false) {
        var event = new Event('change');
        var select_list = Array.from(document.querySelectorAll(selectlist));
        select_list.shift();
        for (var i =  0; i < select_list.length; i++) {
            if(i == index_target) {
                document.querySelector(select_target).value = select_list[i].value;
        }
         };
        if(send){
       document.querySelector(select_target).dispatchEvent(event);
        }    
    }

    // Usage:
    function pesquisar_year(index_ano, index_muni, index_entidade){

        document.querySelector('span > input[name="desp"]').click();
    getAllOptionValues('select#ano > option', 'select[id="ano"]', index_ano); // Ano
    getAllOptionValues('select#municipio > option', 'select[id="municipio"]', index_muni, true); // Municipio

    setTimeout(getAllOptionValues, 3000, 'select#entidade > option', 'select[id="entidade"]', index_entidade);

    setTimeout(() => {
    document.querySelector('input[name="pesquisar"]').click();
    }, 3000);
    };
    """

        script = functions + f"pesquisar_year({index_ano}, {index_municipio}, {index_entidade});"

        self.drive.execute_script(script)

    def acessar_dados(self, index_doc: int):

        script = f"""
    var buttons = document.querySelectorAll('td.text-center > form#form_id')
    buttons[{index_doc}].dispatchEvent(new Event('submit'))
            """
        self.drive.execute_script(script)

        self.wait.until(EC.visibility_of_element_located((By.ID, 'btn-voltar ')))

    def next_page(self):

        script = """
    var page_numbers = document.querySelectorAll('form[class="form-page-numbers float-left"]')
    var next = page_numbers[page_numbers.length - 1]
    if(page_numbers.lenght > 1){
        next.dispatchEvent(new Event('submit'))
    }        
    """
        self.drive.execute_script(script)

    def select_page(self, page: int) -> None:

        script = f"""
            document.querySelector('form[class="form-page-numbers float-left"]:nth-last-child(1) input[name="pg"]').value = "{page}" 
            var next = document.querySelector('form[class="form-page-numbers float-left"]:nth-last-child(1)')
            next.dispatchEvent(new Event('submit'))     
                    """
        try:

            self.drive.execute_script(script)
            sleep(6)
            self.wait.until(EC.visibility_of_element_located((By.ID, 'form_id')))

        except Exception as error:
            # self.register_erro(self.path_erros, self.checkpoint)
            print(f"Falha ao passar a pagina!\n{error}")
            raise error

    def create_slot_tokens(self) -> None:

        script = """
        function create_slot_tokens(){
    var containerDiv = document.createElement("form");
    containerDiv.className = "slot_tokens";
    
    for (var i = 0; i < 21; i++) {
        
        var inputElement = document.createElement('input');
            
        inputElement.type = "text";
        inputElement.name = "g-recaptcha-response";
        inputElement.type = "hidden"
        inputElement.className = "id_validation" + (i + 1);
        inputElement.value = "" + (i + 1)

        containerDiv.appendChild(inputElement);
    }

    document.body.appendChild(containerDiv);
};

create_slot_tokens();
        """
        self.drive.execute_script(script)

    def carregar_tokens(self):

        script = """
        function carregar_tokens(){
    for (var i = 0; i < 21; i++) {
    validar_ids(i + 1)
    }
};

async function validar_ids(n_index){
   await grecaptcha.ready(function() {
            grecaptcha.execute('6Lc5jcsbAAAAADmXWT8NNXy_8mFEu944y99PVFUr', {action:'validate_captcha'})
                      .then(function(token) {
            $('.id_validation' + (n_index)).val(token);
        });
    });

};
carregar_tokens();
        """
        self.drive.execute_script(script)
