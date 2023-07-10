CREATE TABLE rols (
	id uuid NOT NULL PRIMARY KEY,
	nombre varchar(50) NOT NULL,
	abreviacion varchar(3) NOT NULL,
	estado bool NOT NULL DEFAULT true
);
COMMENT ON TABLE rols IS 'Tabla que almacena los roles de los usuarios del sistema';

-- Column comments

COMMENT ON COLUMN rols.id IS 'Identificador de la tabla rols';
COMMENT ON COLUMN rols.nombre IS 'Nombre de rol';
COMMENT ON COLUMN rols.abreviacion IS 'Abreviacion del rol';
COMMENT ON COLUMN rols.estado IS 'Estado del rol 1: activo 0: inactivo';


CREATE TABLE menus (
	id uuid NOT NULL PRIMARY KEY,
	nombre varchar(50) NOT NULL,
	abreviacion varchar(3) NOT NULL,
	url varchar(150) not null,
	estado bool NOT NULL DEFAULT true
);
COMMENT ON TABLE menus IS 'Tabla que almacena los disponbles del sistema';

-- Column comments

COMMENT ON COLUMN menus.id IS 'Identificador de la tabla menus';
COMMENT ON COLUMN menus.nombre IS 'Nombre de menu';
COMMENT ON COLUMN menus.abreviacion IS 'Abreviacion del menu';
COMMENT ON COLUMN menus.url IS 'Url para el acceso a la opcion del menu';
COMMENT ON COLUMN menus.estado IS 'Estado del rol 1: activo 0: inactivo';




CREATE TABLE menu_rols (
	id uuid NOT NULL PRIMARY KEY,
  rol_id uuid,
  menu_id uuid,
  can_udpate bool NOT NULL DEFAULT true,
  can_delete bool NOT NULL DEFAULT true,
  can_view bool NOT NULL DEFAULT true,
	estado bool NOT NULL DEFAULT true,
  CONSTRAINT fk_rol
    FOREIGN KEY(rol_id) 
	  REFERENCES rols(id)
	  ON DELETE cascade,
  CONSTRAINT fk_menu
    FOREIGN KEY(menu_id) 
	  REFERENCES menus(id)
	  ON DELETE CASCADE
);
COMMENT ON TABLE menu_rols IS 'Tabla que almacena las relaciones entre los roles y los menus a los que tienen acceso los roles';

-- Column comments

COMMENT ON COLUMN menu_rols.id IS 'Identificador de la tabla menu_rols';
COMMENT ON COLUMN menu_rols.rol_id IS 'clave foranea de la tabla rols';
COMMENT ON COLUMN menu_rols.menu_id IS 'clave foranea de la tabla menus';
COMMENT ON COLUMN menu_rols.can_udpate IS 'Opcion que establece si el rol puede editar dentro del menu';
COMMENT ON COLUMN menu_rols.can_delete IS 'Opcion que establece si el rol puede eliminar dentro del menu';
COMMENT ON COLUMN menu_rols.can_view IS 'Opcion que establece si el rol puede visualizar dentro del menu';
COMMENT ON COLUMN menu_rols.estado IS 'Estado del rol 1: activo 0: inactivo';



CREATE TABLE users (
	id uuid NOT NULL PRIMARY KEY,
  rol_id uuid,
  nombre varchar(80) not null,
  apellidos varchar(100) not null,
  email varchar(150) not null,
	estado bool NOT NULL DEFAULT true,
  CONSTRAINT fk_user_rol
    FOREIGN KEY(rol_id) 
	  REFERENCES rols(id)
	  ON DELETE CASCADE
);
COMMENT ON TABLE users IS 'Tabla que almacena los usuarios del sistema';

-- Column comments

COMMENT ON COLUMN users.id IS 'Identificador de la tabla users';
COMMENT ON COLUMN users.rol_id IS 'clave foranea de la tabla rols';
COMMENT ON COLUMN users.nombre IS 'nombre registrado del usuario';
COMMENT ON COLUMN users.apellidos IS 'apellidos del usuario (paterno y materno)';
COMMENT ON COLUMN users.email IS 'correo electronico del usuario';
COMMENT ON COLUMN users.estado IS 'Estado del registro 1: activo 0: inactivo';





CREATE TABLE categorias (
	id uuid NOT NULL PRIMARY KEY,
  nombre varchar(50) not null,
  abreviacion varchar(3) not null,
	estado bool NOT NULL DEFAULT true
);
COMMENT ON TABLE categorias IS 'Tabla que almacena las categorias de los ticker generados';

-- Column comments

COMMENT ON COLUMN categorias.id IS 'Identificador de la tabla categorias';
COMMENT ON COLUMN categorias.nombre IS 'Nombre de la categoria';
COMMENT ON COLUMN categorias.abreviacion IS 'Abreviacion de la categoria';
COMMENT ON COLUMN categorias.estado IS 'Estado del registro 1: activo 0: inactivo';





CREATE TABLE tickets (
	id uuid NOT NULL PRIMARY KEY,
  user_id uuid not null,
  categoria_id uuid not null,
  titulo varchar(150) not null,
  descripcion text not null,
	estado int NOT NULL DEFAULT 1,
  CONSTRAINT fk_ticket_user
    FOREIGN KEY(user_id) 
	  REFERENCES users(id)
	  ON DELETE CASCADE,
  CONSTRAINT fk_ticket_categoria
    FOREIGN KEY(categoria_id) 
	  REFERENCES categorias(id)
	  ON DELETE CASCADE
);
COMMENT ON TABLE tickets IS 'Tabla que almacena los tickets registrados por los usuarios';

-- Column comments

COMMENT ON COLUMN tickets.id IS 'Identificador de la tabla tickets';
COMMENT ON COLUMN tickets.user_id IS 'identificador de la tabla users';
COMMENT ON COLUMN tickets.categoria_id IS 'identificador de la tabla cateogoria';
COMMENT ON COLUMN tickets.titulo IS 'Titulo de referencia del ticker';
COMMENT ON COLUMN tickets.descripcion IS 'Descripcion del problema que derivo en la generacion de ticket';
COMMENT ON COLUMN tickets.estado IS 'Estado del registro 1: pendiente, 0: rechazado, 2: Terminado';



CREATE TABLE respuestas (
	id uuid NOT NULL PRIMARY KEY,
  user_id uuid not null,
  ticket_id uuid not null,
  observacion text not null,
  estado_resultante int not null,
  
  CONSTRAINT fk_respuesta_user
    FOREIGN KEY(user_id) 
	  REFERENCES users(id)
	  ON DELETE CASCADE,
  CONSTRAINT fk_respuesta_ticket
    FOREIGN KEY(ticket_id) 
	  REFERENCES tickets(id)
	  ON DELETE CASCADE
);
COMMENT ON TABLE respuestas IS 'Tabla que almacena los tickets registrados por los usuarios';

-- Column comments

COMMENT ON COLUMN respuestas.id IS 'Identificador de la tabla respuesta';
COMMENT ON COLUMN respuestas.user_id IS 'Usuario que registro la respuesta';
COMMENT ON COLUMN respuestas.ticket_id IS 'Ticket al que pertenece la respuesta';
COMMENT ON COLUMN respuestas.observacion IS 'Observacion de la respuesta';
COMMENT ON COLUMN respuestas.estado_resultante IS 'Estado de cambio del ticker';