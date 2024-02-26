# Vue.js Website (genutztes JS Framework):
  - https://vuejs.org/
  - 
# Vue.js Tutorial für Visual Studio Code:
  - https://code.visualstudio.com/docs/nodejs/vuejs-tutorial

# Vue Router (für Navigation auf der Website):
  - https://router.vuejs.org/

# Chart.js für Vue.js (für Darstellung der Daten als Graph):
  - https://vue-chartjs.org/

# Gute Vue.js Tutorials:
  - https://www.youtube.com/watch?v=YrxBCBibVo0&list=PL4cUxeGkcC9hYYGbV60Vq3IXYNfDk8At1

Vue.js, Vue Router und Chart.js wie auf der jeweiligen Website beschrieben mit dem
Node Package Manager (NPM) installieren.
Anschließend einmal "npm install" ausführen!
Am besten in Visual Studio Code noch die "Vue Language Features" Extension installieren ;)

Lokal hosten mit "npm run serve" funktioniert nicht, weil man vom localhost ja keine Zugriffsrechte
auf Leos Server hat.

Daher zum updaten der Live-Website "npm run build" ausführen und anschließend den Website Ordner
auf dem Server durch den dist Ordner ersetzen (diesen dann logischerweise wieder in Website umbenennen)
Assets wie die Icons müssen manuell ins assets Verzeichnis hinzugefügt werden (nur bei Änderung).
