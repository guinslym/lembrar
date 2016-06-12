#intallation
https://github.com/snicoper/django-boilerplate
for using React
https://github.com/AngryDogs/django-wp-react-boilerplate
Maybe I should only use **webpack** and remove __gulp.js__ check **django-wp-react-boilerplate**
## Node

Editar ``./.package.json`` para los paquetes de **nodejs**

    npm install

Para actualizar los paquetes, usar [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)

    sudo npm install -g npm-check-updates

    # Mostrar paquetes con actualizaciones.
    ncu

    # Actualizarlos
    ncu -u

### Scripts en package.json

- ``npm run gulp``: Lo mismo que ``gulp``
- ``npm run sphinx``: Lo mismo que ``gulp sphinx``

## Bower

Actualmente instala

- [JQuery](https://jquery.com/)
- [font-awesome](https://fortawesome.github.io/Font-Awesome/)
- [Bootstrap4](http://v4-alpha.getbootstrap.com)

Instalar bower a nivel global

    sudo npm install bower -g

Los paquetes los instala en ``./src/static/vendor/``

    bower install

Para actualizar los paquetes, usar [npm-check-updates](https://www.npmjs.com/package/npm-check-updates)

    npm install -g npm-check-updates

    ncu -m bower

### gulpfile.js

- ``gulp``: Unifica y minifica los archivos ``.js`` y ``.scss``
- ``gulp style:sass``: Unifica y minifica los archivos ``.scss``
- ``gulp scripts:js``: Unifica y minifica los archivos ``.js``
- ``gulp watch``: Escucha los directorios ``.js`` y ``.scss``.
- ``gulp build-docs``: Re construye los docs Sphinx (``make html``)
- ``gulp sphinx``: Escucha si hay un cambio en ``./docs``.
