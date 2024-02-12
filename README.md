# Wikimedia Kafka Producer Project

Este proyecto captura cambios recientes de Wikimedia y los publica en un tema de Kafka. Utiliza Docker para configurar y ejecutar el entorno de Kafka, incluyendo Zookeeper, Schema Registry, PostgreSQL, y Conduktor para gestión y monitoreo.

## Docker Compose Setup

El archivo `docker-compose.yml` define los servicios necesarios:

### Servicios

- **Zookeeper**: Utilizado por Kafka para la gestión del clúster.
  - Imagen: `confluentinc/cp-zookeeper:7.3.0`
  - Puerto: `2181`

- **Kafka**: El broker de mensajes.
  - Imagen: `confluentinc/cp-kafka:7.3.0`
  - Puertos: `9092`, `29092`, `9999`

- **Schema Registry**: Para gestionar esquemas de Kafka.
  - Imagen: `confluentinc/cp-schema-registry:7.3.0`
  - Puerto: `8081`

- **PostgreSQL**: Base de datos para Conduktor.
  - Imagen: `postgres:14`

- **Conduktor Console**: Interfaz de usuario para gestionar Kafka.
  - Imagen: `conduktor/conduktor-platform:1.18.1`
  - Puerto: `8080`

- **Conduktor Monitoring**: Para monitorear el clúster de Kafka.
  - Imagen: `conduktor/conduktor-platform-cortex:1.18.1`

### Configuración de `platform-config.yml`

Define la configuración para Conduktor, incluyendo detalles de la organización, base de datos, administrador, usuarios y monitoreo.

## Código Python

### `main.py`

Punto de entrada que invoca al productor de Kafka para procesar cambios de Wikimedia.

### `kafka_consumer.py`

Captura y procesa los cambios recientes de Wikimedia, enviándolos a un tema de Kafka.

- **URL de streaming**: `https://stream.wikimedia.org/v2/stream/recentchange`
- **Configuración del Productor Kafka**: Define cómo conectar y enviar mensajes al broker Kafka.

## Ejecución del Proyecto

Para poner en marcha el proyecto, asegúrate de tener Docker y Docker Compose instalados, luego ejecuta:

```bash
docker-compose up -d
```

Esto levantará todos los servicios definidos en `docker-compose.yml`, permitiéndote comenzar a capturar y procesar cambios de Wikimedia a través de Kafka.