const Sequelize = require('sequelize')

const sequelize = new Sequelize('mac_demo' , 'root' , 'SENHA',{
    host:"localhost",
    dialect:'mysql'
})

sequelize.authenticate().then(function(){
        console.log('Conexão com o MySQL foi estabelecida com sucesso')
    }).catch(function (erro){
        console.log('Não foi possível se conectar com o banco de dados MySQL'+erro)
    })  
   
