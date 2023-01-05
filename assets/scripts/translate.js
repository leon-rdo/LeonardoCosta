function translateBR(){
    if(document.querySelector('a[href="#start"]').innerHTML == "Início"){
        alert('Já está em português!')
    } else {location.reload()}
}
function translateEn() {
    if(document.querySelector('a[href="#start"]').innerHTML == "Start"){
        alert("It's already in english!");
    }
    document.querySelector('a[href="#start"]').innerHTML = 'Start';
    document.querySelector('a[href="#Bio"]').innerHTML = 'Biography';
    document.querySelector('a[href="#Formation"]').innerHTML = 'Formation';
    document.querySelector('a[href="#Certificates"]').innerHTML = 'Certificates';
    document.querySelector('a[href="#Achievements"]').innerHTML = 'Achievements';

    document.getElementById('bioTitle').innerHTML = 'Biography';
    document.getElementById('bioFirstP').innerHTML = 'Born in São Gonçalo - Rio de Janeiro, on Friday the 16th of May 2003, Leonardo Matheus de Abreu Costa is a student of Systems Analysis and Development at the University of Amazônia - UNAMA.'
    document.getElementById('bioSecondP').innerHTML = 'At the age of 6 he moved to Belém do Pará, where he lives nowadays. Leonardo is, currently, an intern at Ser Educacional, as a front-end developer.';
    document.getElementById('leokidCap').innerHTML = 'Leonardo at 5 years old.';


    document.getElementById('formationTitle').innerHTML = 'Formation';

    document.getElementById('certificatesTitle').innerHTML = 'Certificates';

    document.getElementById('achievementsTitle').innerHTML = 'Achievements';

    document.getElementById('seeMore').innerHTML = 'See more';

    document.getElementById('contact').innerHTML = 'Contact';

    document.querySelector('#tranlationMessage small').innerHTML = "We're still working on the translation, thank you for the comprehension!";
    document.getElementById('btnEN-into').style.backgroundColor = '#198754';
    document.getElementById('btnEN-into').style.borderColor = '#198754';
    document.getElementById('btnEN-out').style.backgroundColor = '#198754';
    document.getElementById('btnEN-out').style.borderColor = '#198754';

    document.getElementById('btnES-into').style.backgroundColor = '';
    document.getElementById('btnES-into').style.borderColor = '';
    document.getElementById('btnES-out').style.borderColor = '';
    document.getElementById('btnES-out').style.backgroundColor = '';


    document.getElementById('btnBR-out').style.backgroundColor = '#70747c';
    document.getElementById('btnBR-out').style.borderColor = '#70747c';
    document.getElementById('btnBR-into').style.backgroundColor = '#70747c';
    document.getElementById('btnBR-into').style.borderColor = '#70747c';

    itemCard.querySelector('.modelo-card .card-body .card-title').innerHTML = achievementsJSON[i].titleEN;
}
function translateEs() {
    if(document.querySelector('a[href="#start"]').innerHTML == "Comienzo"){
        alert("Ya esta en español!");
    }
    document.querySelector('a[href="#start"]').innerHTML = 'Comienzo';
    document.querySelector('a[href="#Bio"]').innerHTML = 'Biografía';
    document.querySelector('a[href="#Formation"]').innerHTML = 'Capacitación';
    document.querySelector('a[href="#Achievements"]').innerHTML = 'Logros';

    document.getElementById('bioTitle').innerHTML = 'Biografía';
    document.getElementById('bioFirstP').innerHTML = 'Nacido en São Gonçalo - Rio de Janeiro, el viernes 16 de mayo de 2003, Leonardo Matheus de Abreu Costa es estudiante de Análisis y Desarrollo de Sistemas en la Universidad de Amazonia - UNAMA.'
    document.getElementById('bioSecondP').innerHTML = 'A los 6 años se mudó a Belém do Pará, donde vive hasta la actualidad. Leonardo actualmente es pasante en Ser Educacional, como desarrollador front-end.';
    document.getElementById('leokidCap').innerHTML = 'Leonardo a los 5 años.';

    document.getElementById('formationTitle').innerHTML = 'Capacitación';

    document.getElementById('achievementsTitle').innerHTML = 'Logros';

    document.getElementById('seeMore').innerHTML = 'Ver más';

    document.getElementById('contact').innerHTML = 'Contacto';

    document.querySelector('#tranlationMessage small').innerHTML = "Todavía estamos trabajando en la traducción, ¡gracias por la comprensión!";

    document.getElementById('btnEN-into').style.backgroundColor = '';
    document.getElementById('btnEN-into').style.borderColor = '';
    document.getElementById('btnEN-out').style.backgroundColor = '';
    document.getElementById('btnEN-out').style.borderColor = '';

    document.getElementById('btnES-into').style.backgroundColor = '#198754';
    document.getElementById('btnES-into').style.borderColor = '#198754';
    document.getElementById('btnES-out').style.borderColor = '#198754';
    document.getElementById('btnES-out').style.backgroundColor = '#198754';


    document.getElementById('btnBR-out').style.backgroundColor = '#70747c';
    document.getElementById('btnBR-out').style.borderColor = '#70747c';
    document.getElementById('btnBR-into').style.backgroundColor = '#70747c';
    document.getElementById('btnBR-into').style.borderColor = '#70747c';
}
