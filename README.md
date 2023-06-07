# Módulos customizados en la versión 12.0 de Odoo

En este repositorio se encuentran los módulos customizados desarrollados para la versión 12.0 de Odoo, basados en la rama 12.0 de la comunidad de Odoo (OCA/OCB). Estos módulos han sido adaptados y personalizados a partir de desarrollos realizados en diferentes submódulos de la OCA, referenciados en el repositorio de GitHub de la OCA, siempre teniendo en cuenta la rama 12.0.

## Funcionalidades

A continuación se detallan las funcionalidades implementadas en los módulos customizados:

1. **Asociar blogs/noticias a una compañía**

   Descripción:
   Este módulo permite asociar un blog a una única compañía y vincular las noticias a ese blog para heredar automáticamente la compañía. La asociación de la compañía se realiza desde la vista formulario del blog. En la vista de la noticia se muestra la compañía, pero no se puede modificar, ya que hereda la compañía del blog. Los diferentes perfiles de usuarios de Odoo pueden ver y gestionar únicamente los blogs y noticias asociadas a su compañía y a las compañías descendientes.

2. **No permitir pedidos de venta con cantidades cero**

   Descripción:
   Este módulo impide la creación de pedidos de venta con cantidades de productos iguales a cero. Si el usuario intenta confirmar un pedido de venta con cantidades cero, se mostrará una advertencia y se bloqueará la continuación del flujo de venta. Además, se añade un botón en la cabecera del pedido de venta para eliminar las líneas que tengan una cantidad de producto igual a cero. También se han incluido tests unitarios para verificar estas funcionalidades.

3. **Modificaciones en el formulario de contacto de oportunidades**

   Descripción:
   Este módulo personaliza el formulario de contacto en el módulo de oportunidades (CRM) de la siguiente manera:
   - Añade un campo seleccionable en el modelo de la oportunidad para que el usuario indique la fuente a través de la cual encontró la empresa: "Terceros/Redes sociales/Búsqueda en Internet". Este campo se muestra en el formulario tanto en el backend como en el frontend (website).
   - En el formulario de contacto del sitio web, se elimina el campo de teléfono y se hace que la compañía no sea obligatoria. Además, se muestra el campo seleccionable mencionado anteriormente, que será obligatorio y el usuario deberá seleccionar la fuente a través de la cual encontró la empresa: "Terceros/Redes sociales/Búsqueda en Internet".
   - Se ha agregado validación al campo de correo electrónico.

## Requerimientos

- Odoo 12.0
- Dependencias adicionales (indicar si las hay)

## Instalación

1. Clonar este repositorio.
2. Colocar los módulos en la ruta adecuada de Odoo.
3. Reiniciar el servidor Odoo.
4. Actualizar la lista de módulos en Odoo e instalar los módulos customizados.
5. Realizar cualquier otra configuración o requisitos adicionales necesarios.
