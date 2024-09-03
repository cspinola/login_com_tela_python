from tkinter import *
from tkinter import messagebox
from funcoes_de_bd import *
from hashlib import sha256

# Conexão
conexao = conectar_db('Usuarios.db')

# Criar uma tabela
criar_tabela(conexao)

class MinhaGUI:
    def __init__(self):
        self.janela_principal = Tk()
        self.janela_principal.title('Login')
        self.lab = Label(self.janela_principal, text="Login de Usuário")
        self.lab.pack()
        self.janela_principal.geometry('250x150')
        
        self.lab1 = Label(self.janela_principal, text="Insira o nome de usuário:")
        self.lab1.pack()
        self.login = Entry(self.janela_principal)
        self.login.pack()

        self.lab2 = Label(self.janela_principal, text="Insira sua senha de usuário:")
        self.lab2.pack()
        self.senha = Entry(self.janela_principal, show='*')
        self.senha.pack()

        self.btnLogin = Button(self.janela_principal, text='Login', command=self.logar)
        self.btnCad = Button(self.janela_principal, text='ou se Cadastre', command=self.tela_de_cadastro)
        
        self.btnLogin.pack()
        self.btnCad.pack()
        mainloop()
        
    def tela_de_cadastro(self):
        
        self.janela_cadastro = Tk()
        self.janela_cadastro.title('Cadastro')
        self.janela_cadastro.geometry('250x150')
        
        self.lab3 = Label(self.janela_cadastro, text="Cadastro de Usuário")
        self.lab3.pack()
        self.lab4 = Label(self.janela_cadastro, text="Insira o nome de usuário:")
        self.lab4.pack()
        self.login = Entry(self.janela_cadastro)
        self.login.pack()

        self.lab5 = Label(self.janela_cadastro, text="Insira sua senha de usuário:")
        self.lab5.pack()
        self.senha = Entry(self.janela_cadastro, show='*')
        self.senha.pack()
        
        self.btn_cadastrar = Button(self.janela_cadastro, text='Cadastrar', command = self.cadastrar)
        self.btn_cadastrar.pack()


    def cadastrar(self):
        self.conexao = conectar_db('Usuarios.db')
        criar_tabela(self.conexao)
        
        #senha_armazenar = sha256(self.senha.get().encode()).digest()
        
        try:
            inserir_usuario(self.conexao, self.login.get(), self.senha.get())
            messagebox.showinfo('Cadastro realizado com sucesso!','Usuário Cadastrado')
            self.janela_cadastro.destroy()
            
        except:
            messagebox.showinfo('Erro','Usuário inválido ou já cadastrado')
            
        self.conexao = desconecta_bd('Usuarios.db')
    

    
    def logar(self):
        
        self.conexao = conectar_db('Usuarios.db')
        #senha_str = self.senha.get()
        #senha_armazenada = sha256(senha_str.encode()).digest()
        
        try:
            buscar_usuario(self.conexao, self.login.get(), self.senha.get())
            messagebox.showinfo('Login realizado com sucesso!','Usuário Logado')
        
        except:
            messagebox.showinfo('Erro confirmar seu usuário ou senha.','Verifique seu usuário e senha!')
        
        self.conexao = desconecta_bd('Usuarios.db')

gui = MinhaGUI()