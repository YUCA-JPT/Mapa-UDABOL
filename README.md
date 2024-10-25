# Mapa-UDABOL
mapa
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mapa Satelital con Leaflet y Google Maps</title>
  <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
  <style>
    #map {
      height: 600px;
      width: 100%;
    }
  </style>
</head>
<body>

<h3>Mapa Satelital con Leaflet y Google Maps</h3>
<div id="map"></div>

<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
<script src="https://maps.googleapis.com/maps/api/js?key=TU_API_KEY"></script>
<script>
  // Inicializar el mapa
  var map = L.map('map').setView([-17.390744, -66.068831], 17); // Coordenadas iniciales

  // Añadir la capa de Google Maps Satelital
  L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
    maxZoom: 20,
    subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
  }).addTo(map);

  // Definir íconos personalizados
  var icons = {
    'apoyo academico': L.icon({ iconUrl: 'iconos/Apoyo Academico.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'arquitectura': L.icon({ iconUrl: 'iconos/Arquitectura.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'aulas': L.icon({ iconUrl: 'iconos/Aulas.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'aulas g': L.icon({ iconUrl: 'iconos/Aulas G.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'secretaria': L.icon({ iconUrl: 'iconos/Secretaria.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'aula docente': L.icon({ iconUrl: 'iconos/Aula Docentes.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'baño administrativo': L.icon({ iconUrl: 'iconos/Baño Administrativo.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'baño': L.icon({ iconUrl: 'iconos/Baño.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'biblioteca': L.icon({ iconUrl: 'iconos/Biblioteca.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'cajas': L.icon({ iconUrl: 'iconos/Cajas.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'cartera': L.icon({ iconUrl: 'iconos/Cartera.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'centro de computos': L.icon({ iconUrl: 'iconos/Centro de Computos.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'comedor': L.icon({ iconUrl: 'iconos/Comedor.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'fotocopias': L.icon({ iconUrl: 'iconos/Fotocopias.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'informacion': L.icon({ iconUrl: 'iconos/Informacion.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'investigacion': L.icon({ iconUrl: 'iconos/Investigacion.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'jefatura': L.icon({ iconUrl: 'iconos/Jefatura.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'medicina': L.icon({ iconUrl: 'iconos/Medicina.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'piscina': L.icon({ iconUrl: 'iconos/Piscina.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'laboratorio de telecom': L.icon({ iconUrl: 'iconos/Laboratorio de Telecom.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'sala audiovisual': L.icon({ iconUrl: 'iconos/Sala Audiovisual.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
    'sala de estudiantes': L.icon({ iconUrl: 'iconos/Sala de Estudiantes.png', iconSize: [32, 32], iconAnchor: [16, 32] }),
  };

  // Coordenadas de las aulas desde el CSV (ahora con el campo 'tipo' incluido)
        var aulas = [
          { aula: 'Cc1', coords: [-17.390790, -66.06878], descripcion: 'Ingenieria/Arquitectura', tipo: 'centro de computos' },
          { aula: 'Cc2', coords: [-17.390740, -66.06875], descripcion: 'Ingenieria/Arquitectura', tipo: 'centro de computos' },
          { aula: 'Cc3', coords: [-17.390690, -66.06872], descripcion: 'Ingenieria/Arquitectura', tipo: 'centro de computos' },
          { aula: 'Cc4', coords: [-17.390640, -66.06869], descripcion: 'Ingenieria/Arquitectura', tipo: 'centro de computos' },
          { aula: 'C1', coords: [-17.390375, -66.068930], descripcion: 'Medicina', tipo: 'medicina' },
          { aula: 'C2', coords: [-17.390400, -66.068890], descripcion: 'Medicina', tipo: 'medicina' },
          { aula: 'C3', coords: [-17.390437, -66.068830], descripcion: 'Medicina', tipo: 'medicina' },
          { aula: 'C4', coords: [-17.390474, -66.068760], descripcion: 'Medicina', tipo: 'medicina' },
          { aula: 'D1', coords: [-17.390620, -66.068504], descripcion: 'Arquitectura', tipo: 'arquitectura' },
          { aula: 'D2', coords: [-17.390605, -66.068527], descripcion: 'Arquitectura', tipo: 'arquitectura' },
          { aula: 'D3', coords: [-17.390575, -66.068576], descripcion: 'Arquitectura', tipo: 'arquitectura' },
          { aula: 'D4', coords: [-17.390545, -66.068625], descripcion: 'Arquitectura', tipo: 'arquitectura' },
          { aula: 'D5', coords: [-17.390516, -66.068681], descripcion: 'Arquitectura', tipo: 'arquitectura' },
          { aula: 'A1', coords: [-17.390853, -66.069033], descripcion: 'Medicina', tipo: 'medicina' },
          { aula: 'A2', coords: [-17.390895, -66.068956], descripcion: 'Medicina', tipo: 'medicina' },
          //{ aula: 'A3', coords: [-17.39102474171155, -66.06875205134645], descripcion: 'Medicina', tipo: 'medicina' },
          { aula: 'Informacion y Marqueting', coords: [-17.390935, -66.068876], descripcion: 'Información y Marketing', tipo: 'informacion' },
        // { aula: 'Chicas', coords: [-17.390409,-66.068357], descripcion: 'AREAS DE SANIDAD', tipo: 'baño' },
          { aula: 'Chicos', coords: [-17.390409,-66.068357], descripcion: 'Medicina', tipo: 'baño' },
          { aula: 'Piscina', coords: [-17.390460477082208, -66.0681858430601], descripcion: 'AREAS DE CONVIVENCIA', tipo: 'piscina' },
          { aula: 'Comedor', coords: [-17.390432, -66.067859], descripcion: 'AREAS DE CONVIVENCIA', tipo: 'comedor' },
          { aula: 'Jefaturas', coords: [-17.390530, -66.068320], descripcion: 'planta baja', tipo: 'jefatura' },
          { aula: 'Biblioteca', coords: [-17.390896, -66.068460], descripcion: 'Biblioteca', tipo: 'biblioteca' },
          { aula: 'Cajas-Ventanilla Unica', coords: [-17.390835, -66.068485], descripcion: 'planta baja', tipo: 'cajas' },
          { aula: 'Sala Audio Visual', coords: [-17.390940452135812, -66.06870538980458], descripcion: 'Sala Audio Visual', tipo: 'sala audiovisual' },
          { aula: 'Fotocopiadora', coords: [-17.390888795550488, -66.06875162673037], descripcion: 'Fotocopiadora', tipo: 'fotocopias' },
          { aula: 'Apoyo Académico', coords: [-17.390668, -66.068456], descripcion: 'Apoyo Académico', tipo: 'apoyo academico' },
          { aula: 'Sala de Estudiantes',coords:[-17.390635, -66.068430], descripcion: 'Sala de Estudiantes', tipo: 'sala de estudiantes' },
          ///{ aula: 'Cartera', coords: [-17.390620, -66.068343], descripcion: 'Cartera', tipo: 'cartera' },
          { aula: 'Aulas Docente', coords: [-17.390641, -66.068367], descripcion: 'Aulas Docente', tipo: 'aula docente' },
          { aula: 'Aula T3', coords: [-17.390750, -66.068310], descripcion: 'Planta Baja', tipo: 'aulas' },
          { aula: 'Laboratorio de Telecom', coords: [-17.390830, -66.068270], descripcion: 'planta baja', tipo: 'laboratorio de telecom' },
          { aula: 'Secretaria Regional', coords: [-17.390810, -66.068420], descripcion: 'planta baja', tipo: 'secretaria' },
          
          //{ aula: 'Sala de Investigacion', coords: [-17.390681, -66.068340], descripcion: 'Sala de Investigación', tipo: 'investigacion' },
          { aula: 'Aula G-12, G-5', coords: [-17.390820, -66.068369], descripcion: 'piso 1', tipo: 'aulas g' },
          { aula: 'Baños Administrativos', coords: [-17.390749, -66.068489], descripcion: 'piso 1', tipo: 'baño administrativo' },
          //{ aula: 'Aula G-16', coords: [-17.390679, -66.068302], descripcion: 'Aula G', tipo: 'aulas g' },
          { aula: 'Aula G-16, G-19', coords: [-17.390700, -66.068377], descripcion: 'Aula G', tipo: 'aulas g' },
          { aula: 'Aula G-17, G-18', coords: [-17.390783, -66.068415], descripcion: 'piso 2', tipo: 'aulas g' }
        ];


  // Añadir los marcadores al mapa con íconos personalizados
  aulas.forEach(function(punto) {
    var icono = icons[punto.tipo] || icons['aulas']; // Asigna el ícono basado en el tipo, o el ícono de aulas si no se especifica
    var marker = L.marker(punto.coords, { icon: icono }).addTo(map);
    marker.bindPopup(`<b>${punto.aula}</b><br>${punto.descripcion}`);
    
    //var aulaMarker = L.marker([latitude, longitude]).addTo(map);
    //aulaMarker.bindPopup("<b>Aula 101</b><br>Capacidad: 30 alumnos.<br>Edificio A, planta baja.");
  //aulaMarker.bindTooltip("Aula 101").openTooltip();  // Tooltip al pasar el mouse
  });

    // Coordenadas de la ruta entre dos aulas o edificios
      var routePalliso = [ // entrada puerta principal y pasillo
        [-17.390699,-66.069058],[-17.390915,-66.068647],   // Coordenada de entrada a pasillo
        [-17.391074,-66.068745],[-17.390479,-66.068378], //pasillo
        [-17.390409,-66.068357],// punto baño
      ];var route1 = L.polyline(routePalliso, { color:'blue', weight: 4 }).addTo(map); //entrada principal a pasillos y Baños mujer, varones
      
      var routeC1= [
        [-17.390375,-66.068953],[-17.390639,-66.068479], //coordenada de aulas de C1 A d1
      ];var route1 = L.polyline(routeC1, { color: 'blue', weight: 4 }).addTo(map);
      
      var routeCC1 = [
        [-17.390562,-66.068620],[-17.390840,-66.068786],  //coordenada aulas Cc1 a cc4
      ];var route1 = L.polyline(routeCC1, { color:'blue', weight: 4 }).addTo(map);

    var routeA = [
      [-17.390729,-66.069006],[-17.390841,-66.069074],  //pasillo a1, a2, marketing
      [-17.390967,-66.068842],[-17.390850,-66.068772],  //pasillo a1, a2, marketing
    ];var route1 = L.polyline(routeA,{ color: 'blue', weight: 4 }).addTo(map);
    
    var routeCo = [
      [-17.390432, -66.067859], // punto comedor
      [-17.390535, -66.068086], //punto pisina
      [-17.390470, -66.068374],  // paso esquina 
    ];var route1 = L.polyline(routeCo, { color: 'blue', weight:4 }).addTo(map);

    var routebiblio = [ //ruta biblioteca y caja unica y ventanilla
      [-17.390885, -66.068460],
      [-17.390816, -66.068581],
    ];var route1 = L.polyline(routebiblio,{ color:'blue', weight:4 }).addTo(map);
    

    var routeLb = [ // piso uno, entrada alaboratorio de computo
      [-17.390579, -66.068436],[-17.390609, -66.068386],
      [-17.390688, -66.068432],[-17.390785, -66.068276],
      [-17.390705, -66.068406],[-17.390732, -66.068425],
      [-17.390715, -66.068456],[-17.390720, -66.068459],
      [-17.390743, -66.068419],[-17.390763, -66.068433],
      [-17.390730, -66.068489],[-17.390780, -66.068404],
      //[-17.390723, -66.068369],[-17.390809 , -66.06822],
    ];var route1 = L.polyline(routeLb, { color: 'blue', weight:4 }).addTo(map);
        
    var routeP1 = [ // ruta para g6
      [-17.390545, -66.068418],[-17.390546, -66.068409],
      [-17.390536, -66.068399],[-17.390555, -66.068372],
      [-17.390549, -66.068368],[-17.390547, -66.068360],
      [-17.390553, -66.068350],[-17.390543, -66.068330], 
      [-17.390553, -66.068300],
      [-17.390578, -66.068295], 
    ];var route1 = L.polyline(routeP1, { color: '#9b00ff', weight:4 }).addTo(map);// pisos 1 pa g-9


    var routePiso1 = [ 
      [-17.390705, -66.068406],
      [-17.390732, -66.068425],
      [-17.390715, -66.068456],
      [-17.390720, -66.068459],
      [-17.390743, -66.068419],
      [-17.390763, -66.068433],
      [-17.390730, -66.068489],
      [-17.390780, -66.068404],
      [-17.390720, -66.068369],
      [-17.390809 , -66.068229],
    ];var route1 = L.polyline(routePiso1, { color: '#9b00ff', weight: 4 }).addTo(map); //piso1
  
          
    var routeCoordinates4 = [ //piso 2 g-16,g-17,g-18,g-19
      [-17.390555, -66.068372],
      [-17.390565, -66.068366], 
      [-17.390578, -66.068362],
      [-17.390578, -66.068362],
      [-17.390583, -66.068348],
      [-17.390561, -66.068330],
      [-17.390561, -66.068320],
      [-17.390569, -66.068315],
      [-17.390592, -66.068330],                  
      [-17.390622, -66.068282],
      [-17.390814, -66.068410],
      ];var route1 = L.polyline(routeCoordinates4, { color: '#ff00e0', weight:4 }).addTo(map); //piso2
          
       
   </script>
   <input type="text" id="searchBox" placeholder="Buscar aula..." />

   <script>
     document.getElementById('searchBox').addEventListener('input', function(e) {
       var searchText = e.target.value.toLowerCase();
       map.eachLayer(function (layer) {
         if (layer instanceof L.Marker && layer.getPopup().getContent().toLowerCase().includes(searchText)) {
           layer.openPopup();
         } else {
           layer.closePopup();
         }
       });
     });
   </script>




   

     </body>
</html>
