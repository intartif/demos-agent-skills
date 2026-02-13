# 📋 Plantilla de Workflow Reusable - Guía de Uso

## 🎯 Características

Esta plantilla incluye:

- ✅ **Preparación**: Extracción automática de metadata (versión, nombre, commit, actor)
- ✅ **SonarQube**: Análisis de código estático con Quality Gate
- ✅ **Snyk**: Escaneo de seguridad (código + dependencias)
- ✅ **Build**: Soporte para Node.js, Maven, Gradle
- ✅ **Deploy**: Despliegue con health check
- ✅ **Multi-jobs**: Escaneos en paralelo para mayor velocidad

## 🚀 Uso Básico

### Ejemplo 1: Llamada Simple

```yaml
name: Deploy to Dev

on:
  push:
    branches: [develop]

jobs:
  pipeline:
    uses: tu-org/workflows/.github/workflows/reusable-pipeline-template.yml@main
    with:
      environment: dev
    secrets:
      SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

### Ejemplo 2: Con Opciones

```yaml
name: Deploy to Production

on:
  push:
    tags:
      - 'v*'

jobs:
  pipeline:
    uses: tu-org/workflows/.github/workflows/reusable-pipeline-template.yml@main
    with:
      environment: production
      ref: ${{ github.ref }}
      run-sonar: true
      run-snyk: true
      deploy-enabled: true
    secrets:
      SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
```

### Ejemplo 3: Solo Build (sin deploy)

```yaml
name: Build PR

on:
  pull_request:

jobs:
  build:
    uses: tu-org/workflows/.github/workflows/reusable-pipeline-template.yml@main
    with:
      environment: dev
      deploy-enabled: false  # Solo build, no deploy
    secrets:
      SONAR_TOKEN: ${{ secrets.SONAR_TOKEN }}
      SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}
```

### Ejemplo 4: Usar Outputs

```yaml
jobs:
  pipeline:
    uses: tu-org/workflows/.github/workflows/reusable-pipeline-template.yml@main
    with:
      environment: staging
    secrets:
      DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
  
  notify:
    needs: pipeline
    runs-on: ubuntu-latest
    steps:
      - name: Notify team
        run: |
          echo "App: ${{ needs.pipeline.outputs.app-name }}"
          echo "Version: ${{ needs.pipeline.outputs.version }}"
          echo "URL: ${{ needs.pipeline.outputs.deployment-url }}"
```

## 📝 Inputs

| Input | Tipo | Requerido | Default | Descripción |
|-------|------|-----------|---------|-------------|
| `environment` | string | ✅ Sí | - | Entorno de destino (dev, staging, prod) |
| `ref` | string | ❌ No | '' | Git ref específico para checkout |
| `run-sonar` | boolean | ❌ No | true | Ejecutar análisis de SonarQube |
| `run-snyk` | boolean | ❌ No | true | Ejecutar escaneo de Snyk |
| `deploy-enabled` | boolean | ❌ No | true | Habilitar deployment |

## 🔐 Secrets

| Secret | Requerido | Descripción |
|--------|-----------|-------------|
| `SONAR_TOKEN` | Opcional | Token de SonarQube (requerido si `run-sonar: true`) |
| `SNYK_TOKEN` | Opcional | Token de Snyk (requerido si `run-snyk: true`) |
| `DEPLOY_TOKEN` | Opcional | Token para deployment (requerido si `deploy-enabled: true`) |

## 📤 Outputs

| Output | Descripción |
|--------|-------------|
| `version` | Versión de la aplicación extraída |
| `app-name` | Nombre de la aplicación |
| `deployment-url` | URL del deployment |

## ⚙️ Configuración

### 1. Variables de GitHub

Configura en **Settings → Variables**:

```
SONAR_HOST_URL = https://sonarqube.tu-empresa.com
```

### 2. Secrets de GitHub

Configura en **Settings → Secrets**:

```
SONAR_TOKEN = tu-sonar-token
SNYK_TOKEN = tu-snyk-token
DEPLOY_TOKEN = tu-deploy-token
```

### 3. Archivo de Proyecto

La plantilla detecta automáticamente el tipo de proyecto:

**Node.js** (package.json):
```json
{
  "name": "mi-app",
  "version": "1.2.3",
  "scripts": {
    "build": "..."
  }
}
```

**Maven** (pom.xml):
```xml
<project>
  <artifactId>mi-app</artifactId>
  <version>1.2.3</version>
</project>
```

**Gradle** (build.gradle):
```gradle
version = '1.2.3'
```

## 🔧 Personalización

### Agregar Más Lenguajes/Frameworks

En el job `build`, agrega tu stack:

```yaml
# Python
- name: Setup Python
  if: hashFiles('requirements.txt') != ''
  uses: actions/setup-python@v4
  with:
    python-version: '3.11'

- name: Build Python
  if: hashFiles('requirements.txt') != ''
  run: |
    pip install -r requirements.txt
    python setup.py build
```

### Personalizar Deployment

Modifica el step "Deploy" en el job `deploy`:

```yaml
- name: Deploy
  run: |
    # AWS S3
    aws s3 sync dist/ s3://bucket-${{ inputs.environment }}/
    
    # Kubernetes
    kubectl set image deployment/app app=image:${{ needs.prepare.outputs.version }}
    
    # Docker
    docker build -t app:${{ needs.prepare.outputs.version }} .
    docker push app:${{ needs.prepare.outputs.version }}
    
    # Terraform
    terraform apply -var="version=${{ needs.prepare.outputs.version }}"
```

### Agregar Tests

Después del job `build`:

```yaml
test:
  name: Run Tests
  runs-on: ubuntu-latest
  needs: build
  steps:
    - name: Download artifacts
      uses: actions/download-artifact@v4
      
    - name: Run tests
      run: npm test
```

## 📊 Flujo de Ejecución

```
prepare
   ├─> sonar-scan  ─┐
   └─> snyk-scan   ─┤
                     ├─> build ─> deploy
```

**Tiempo aproximado:**
- Prepare: ~30 segundos
- Sonar + Snyk (paralelo): ~2-5 minutos
- Build: ~1-3 minutos
- Deploy: ~1-2 minutos

**Total: ~5-10 minutos**

## 🎨 Ejemplos Completos

### Pipeline Completo con Múltiples Entornos

```yaml
name: Complete Pipeline

on:
  push:
    branches: [main, develop]
  pull_request:

jobs:
  # PR: Solo build
  pr-build:
    if: github.event_name == 'pull_request'
    uses: ./.github/workflows/reusable-pipeline-template.yml
    with:
      environment: dev
      deploy-enabled: false
    secrets: inherit

  # Develop: Deploy a dev
  dev-deploy:
    if: github.ref == 'refs/heads/develop'
    uses: ./.github/workflows/reusable-pipeline-template.yml
    with:
      environment: dev
    secrets: inherit

  # Main: Deploy a staging y luego production
  staging-deploy:
    if: github.ref == 'refs/heads/main'
    uses: ./.github/workflows/reusable-pipeline-template.yml
    with:
      environment: staging
    secrets: inherit

  production-deploy:
    needs: staging-deploy
    if: github.ref == 'refs/heads/main'
    uses: ./.github/workflows/reusable-pipeline-template.yml
    with:
      environment: production
      run-sonar: false  # Ya se ejecutó en staging
      run-snyk: false   # Ya se ejecutó en staging
    secrets: inherit
```

### Pipeline con Aprobación Manual

```yaml
name: Deploy to Production

on:
  workflow_dispatch:
    inputs:
      version:
        description: 'Version to deploy'
        required: true

jobs:
  deploy:
    uses: ./.github/workflows/reusable-pipeline-template.yml
    with:
      environment: production  # Requiere aprobación si está configurado
      ref: refs/tags/v${{ inputs.version }}
    secrets: inherit
```

## 🐛 Troubleshooting

### SonarQube falla

**Error**: "Quality Gate failed"

**Solución**:
```yaml
# Hacer el Quality Gate opcional
- name: Quality Gate
  continue-on-error: true  # <-- Agregar esto
```

### Snyk encuentra vulnerabilidades

**Error**: "Vulnerabilities found"

**Solución**:
```yaml
# Ajustar el threshold o hacer opcional
- name: Snyk Test
  run: snyk test --severity-threshold=critical  # Solo critical
  continue-on-error: true  # O hacer opcional
```

### Build falla por falta de dependencias

**Solución**: Agregar cache:

```yaml
- name: Cache dependencies
  uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
```

### No se detecta la versión correctamente

**Solución**: Personalizar el step de metadata:

```yaml
- name: Extract metadata
  run: |
    # Para .NET
    VERSION=$(grep '<Version>' *.csproj | sed 's/.*<Version>\(.*\)<\/Version>.*/\1/')
    
    # Para Python setup.py
    VERSION=$(python setup.py --version)
    
    # Hardcoded
    VERSION="1.0.0"
```

## 📚 Recursos

- [GitHub Actions - Reusing Workflows](https://docs.github.com/en/actions/using-workflows/reusing-workflows)
- [SonarQube GitHub Action](https://github.com/SonarSource/sonarqube-scan-action)
- [Snyk GitHub Actions](https://github.com/snyk/actions)

## ✅ Checklist de Implementación

- [ ] Copiar `reusable-pipeline-template.yml` al repo de workflows
- [ ] Configurar secrets (SONAR_TOKEN, SNYK_TOKEN, DEPLOY_TOKEN)
- [ ] Configurar variable SONAR_HOST_URL
- [ ] Personalizar lógica de deployment
- [ ] Crear workflow que llame a la plantilla
- [ ] Probar con PR primero (deploy-enabled: false)
- [ ] Verificar outputs y metadata
- [ ] Configurar environments con aprobaciones (opcional)
- [ ] Ajustar thresholds de seguridad según necesidad

## 💡 Tips

1. **Usa `secrets: inherit`** para pasar todos los secrets automáticamente
2. **Configura environments** en GitHub para aprobaciones manuales
3. **Ajusta los thresholds** de Snyk según tu tolerancia al riesgo
4. **Usa `continue-on-error: true`** para scans no bloqueantes
5. **Cache las dependencias** para builds más rápidos
6. **Monitorea los tiempos** y optimiza jobs lentos

---

¡Listo para usar! 🚀
