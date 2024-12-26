function sub(event){
    event.preventDefault();
    let user=document.getElementById("username").value;
    let email=document.getElementById("email").value;
    let pas=document.getElementById("password").value;
    let cpas=document.getElementById("confirm-password").value
    let len=10;
    let reuser=/^[A-Z][a-zA-z]*$/
    let reemail=/^[a-z][a-z0-9]*@gmail\.com$/;
    let repas=/^[0-9]+$/
    if (( !reuser.test(user)) && (user.length<len)){
        document.getElementById("usermsg").innerText="* User First charater should be Capital letter.\n* User name should not contains numbers and Special Characters.\n*User name should be less than 10 Characters.";
        setTimeout(function () {
            location.reload(); 
        }, 3000);
    }
    else{
        document.getElementById("usermsg").innerText="";
        if (!reemail.test(email)){
            document.getElementById("emailmsg").innerText="Please Enter Valid Email."
            setTimeout(function () {
                location.reload(); 
            }, 3000);
        }
        else{
            document.getElementById("emailmsg").innerText="";
            if (!repas.test(pas)){
                document.getElementById("pasmsg").innerText="Password Should contains Only Numbers"
                setTimeout(function () {
                    location.reload(); 
                }, 3000);
            }
            else{
                document.getElementById("pasmsg").innerText="";
                if(pas!=cpas){
                    document.getElementById("msg1").innerText="Password and Conform Password not matching"
                    setTimeout(function () {
                        location.reload(); 
                    }, 3000);
                }
                else {
                    setTimeout(function () {
                        location.reload(); 
                    }, 3000);
                    document.getElementById("Myform").submit();
                }
            }
        }
    }

   
}