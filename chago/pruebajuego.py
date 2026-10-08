 import * as THREE from 'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

    const root = document.querySelector('#game');
    const overlay = document.querySelector('#overlay');  
    const startButton = document.querySelector('#start-button');
    const overlayCopy = document.querySelector('#overlay-copy');
    const aliveLabel = document.querySelector('#alive-count');
    const healthFill = document.querySelector('#health-fill');
    const healthLabel = document.querySelector('#health-value');
    const ammoLabel = document.querySelector('#ammo-count');
    const killLabel = document.querySelector('#kill-count');
    const statusLabel = document.querySelector('#match-status');
    const messageLabel = document.querySelector('#message');
    const crosshair = document.querySelector('#crosshair');
    const touchControls = document.querySelector('#touch-controls');
    const scene = new THREE.Scene();
    scene.background = new THREE.Color('#aab7a5');
    scene.fog = new THREE.Fog('#aab7a5', 42, 112);
    const camera = new THREE.PerspectiveCamera(75, innerWidth / innerHeight, 0.1, 140);
    camera.rotation.order = 'YXZ';
    const renderer = new THREE.WebGLRenderer({ antialias: true, powerPreference: 'high-performance' });
    renderer.setPixelRatio(Math.min(devicePixelRatio, 1.7));
    renderer.setSize(innerWidth, innerHeight);
    renderer.shadowMap.enabled = true;
    renderer.shadowMap.type = THREE.PCFSoftShadowMap;
    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.15;
    root.appendChild(renderer.domElement);

    scene.add(new THREE.HemisphereLight('#e8f3d9', '#444d3c', 2.15));
    const sun = new THREE.DirectionalLight('#fff1d1', 3.1);
    sun.position.set(-24, 38, 18);
    sun.castShadow = true;
    sun.shadow.mapSize.set(1536, 1536);
    sun.shadow.camera.left = -48;
    sun.shadow.camera.right = 48;
    sun.shadow.camera.top = 48;
    sun.shadow.camera.bottom = -48;
    scene.add(sun);

    const ground = new THREE.Mesh(new THREE.PlaneGeometry(110, 110), new THREE.MeshStandardMaterial({ color: '#7f8970', roughness: 1 }));
    ground.rotation.x = -Math.PI / 2;
    ground.position.y = -0.13;
    ground.receiveShadow = true;
    scene.add(ground);
    const grid = new THREE.GridHelper(100, 50, '#a7b28f', '#89957b');
    grid.position.y = -0.1;
    grid.material.transparent = true;
    grid.material.opacity = 0.18;
    scene.add(grid);

    const obstacleMeshes = [];
    const obstacles = [];
    function addCover(x, z, width, depth, height, color, kind = 'box') {
      const geometry = kind === 'cylinder'
        ? new THREE.CylinderGeometry(width / 2, width / 2, height, 12)
        : new THREE.BoxGeometry(width, height, depth);
      const material = new THREE.MeshStandardMaterial({ color, roughness: .86, metalness: .04 });
      const mesh = new THREE.Mesh(geometry, material);
      mesh.position.set(x, height / 2, z);
      mesh.castShadow = true;
      mesh.receiveShadow = true;
      scene.add(mesh);
      obstacleMeshes.push(mesh);
      obstacles.push({ x, z, halfX: width / 2 + .55, halfZ: (kind === 'cylinder' ? width : depth) / 2 + .55 });
      if (kind !== 'cylinder') {
        const stripe = new THREE.Mesh(new THREE.BoxGeometry(width + .025, .07, depth + .025), new THREE.MeshStandardMaterial({ color: '#d7fb61', roughness: .75 }));
        stripe.position.set(x, height * .72, z);
        scene.add(stripe);
      }
    }

    function addTree(x, z, scale = 1) {
      const trunk = new THREE.Mesh(new THREE.CylinderGeometry(.18 * scale, .25 * scale, 2.1 * scale, 8), new THREE.MeshStandardMaterial({ color: '#554b36', roughness: 1 }));
      trunk.position.set(x, 1.05 * scale, z);
      trunk.castShadow = true;
      scene.add(trunk);
      const crown = new THREE.Mesh(new THREE.IcosahedronGeometry(1.15 * scale, 1), new THREE.MeshStandardMaterial({ color: '#53684a', roughness: 1, flatShading: true }));
      crown.position.set(x, 2.45 * scale, z);
      crown.castShadow = true;
      scene.add(crown);
    }

    // Keep an open lane through the center; the low cover makes firefights readable.
    addCover(-12, -9, 8, 2, 2.8, '#65715d');
    addCover(13, -11, 8, 2, 2.8, '#777661');
    addCover(-14, 12, 7, 2.2, 2.3, '#777661');
    addCover(12, 13, 8, 2, 2.8, '#65715d');
    addCover(0, -17, 2.4, 5, 1.5, '#938866');
    addCover(-1, 17, 2.5, 5, 1.5, '#938866');
    addCover(-23, 0, 2, 7, 2.5, '#707966');
    addCover(23, 1, 2, 7, 2.5, '#707966');
    addCover(-7, 2, 2.2, 2.2, 1.65, '#9b7956', 'cylinder');
    addCover(8, -1, 2.2, 2.2, 1.65, '#9b7956', 'cylinder');
    addCover(-5, -25, 4, 2, 1.8, '#6e7963');
    addCover(6, 25, 4, 2, 1.8, '#6e7963');
    for (const [x, z, scale] of [[-34,-27,1.1],[-30,25,.9],[33,-26,1],[35,26,1.2],[-39,2,.85],[39,-3,.9],[-23,36,1],[24,-37,1]]) addTree(x, z, scale);

    const ring = new THREE.Mesh(new THREE.TorusGeometry(39, .08, 5, 150), new THREE.MeshBasicMaterial({ color: '#d7fb61', transparent: true, opacity: .55 }));
    ring.rotation.x = Math.PI / 2;
    ring.position.y = .08;
    scene.add(ring);
    for (const [x, z] of [[-39,-39],[39,-39],[-39,39],[39,39]]) {
      const beacon = new THREE.Mesh(new THREE.CylinderGeometry(.11,.11,4,8), new THREE.MeshBasicMaterial({ color: '#d7fb61' }));
      beacon.position.set(x, 2, z);
      scene.add(beacon);
    }

    const palette = ['#e87554','#4cb9ad','#e5bd55','#c77ab0','#6ba2db','#e7e5db','#91bd58','#de896b','#72c1d2'];
    const bots = [];
    const tracers = [];
    const raycaster = new THREE.Raycaster();
    const center = new THREE.Vector2(0, 0);
    const clock = new THREE.Clock();
    const held = Object.create(null);
    const player = { position: new THREE.Vector3(0, 0, 5), yaw: 0, pitch: 0, health: 100, ammo: 12, kills: 0, alive: true, reloading: false, lastShot: 0, invulnerable: 0, lastHitBy: null };
    let running = false;
    let ended = false;
    let lastMessageUntil = 0;
    let touchLookPointer = null;
    let touchLookX = 0;
    let touchLookY = 0;

    function makePerson(color, isPlayer = false) {
      const group = new THREE.Group();
      const suit = new THREE.MeshStandardMaterial({ color, roughness: .63, metalness: .1 });
      const dark = new THREE.MeshStandardMaterial({ color: '#252c28', roughness: .72, metalness: .15 });
      const skin = new THREE.MeshStandardMaterial({ color: '#d0a17a', roughness: .85 });
      function part(geometry, material, x, y, z) {
        const mesh = new THREE.Mesh(geometry, material);
        mesh.position.set(x, y, z);
        mesh.castShadow = true;
        group.add(mesh);
        return mesh;
      }
      part(new THREE.BoxGeometry(.66, .78, .36), suit, 0, 1.02, 0);
      part(new THREE.SphereGeometry(.23, 12, 10), skin, 0, 1.59, 0);
      part(new THREE.BoxGeometry(.72, .15, .4), dark, 0, 1.36, 0);
      const leftArm = part(new THREE.BoxGeometry(.19, .62, .2), suit, -.43, 1.03, -.03);
      const rightArm = part(new THREE.BoxGeometry(.19, .62, .2), suit, .43, 1.03, -.13);
      leftArm.rotation.z = -.12;
      rightArm.rotation.z = .12;
      part(new THREE.BoxGeometry(.22, .62, .25), dark, -.19, .37, 0);
      part(new THREE.BoxGeometry(.22, .62, .25), dark, .19, .37, 0);
      const pistol = part(new THREE.BoxGeometry(.12, .14, .36), dark, .44, .93, -.36);
      pistol.rotation.x = -.08;
      group.userData.parts = group.children.slice();
      if (isPlayer) group.visible = false;
      return group;
    }

    function randomSpawn(index) {
      const angle = index * Math.PI * 2 / 9 + Math.random() * .25;
      const radius = 24 + Math.random() * 7;
      return new THREE.Vector3(Math.cos(angle) * radius, 0, Math.sin(angle) * radius);
    }

    function resetMatch() {
      for (const bot of bots) scene.remove(bot.mesh);
      bots.length = 0;
      for (const tracer of tracers) scene.remove(tracer.mesh);
      tracers.length = 0;
      player.position.set(0, 0, 5);
      player.yaw = 0;
      player.pitch = 0;
      player.health = 100;
      player.ammo = 12;
      player.kills = 0;
      player.alive = true;
      player.reloading = false;
      player.lastShot = 0;
      player.invulnerable = 2;
      player.lastHitBy = null;
      ended = false;
      camera.position.set(player.position.x, 1.62, player.position.z);
      camera.rotation.set(0, 0, 0);
      for (let i = 0; i < 9; i++) {
        const spawn = randomSpawn(i);
        const mesh = makePerson(palette[i]);
        mesh.position.copy(spawn);
        const bot = { id: i, mesh, position: spawn.clone(), health: 100, alive: true, speed: 2.25 + Math.random() * .65, target: null, think: Math.random(), shoot: Math.random(), strafe: Math.random() < .5 ? -1 : 1, lastHitBy: null };
        scene.add(mesh);
        bots.push(bot);
      }
      updateHud();
      statusLabel.textContent = 'COMBATE ACTIVO';
      showMessage('QUE EMPIECE EL COMBATE');
    }

    function livingCombatants() {
      return bots.filter(bot => bot.alive);
    }

    function updateHud() {
      const alive = livingCombatants().length + (player.alive ? 1 : 0);
      aliveLabel.innerHTML = `${alive.toString().padStart(2, '0')} <small style="font-size:13px;color:var(--muted)">/ 10</small>`;
      healthLabel.textContent = Math.max(0, Math.ceil(player.health));
      healthFill.style.width = `${Math.max(0, player.health)}%`;
      healthFill.style.background = player.health < 35 ? 'var(--red)' : 'var(--lime)';
      ammoLabel.textContent = player.reloading ? '···' : player.ammo.toString().padStart(2, '0');
      killLabel.textContent = player.kills.toString().padStart(2, '0');
    }

    function showMessage(text, duration = 1300) {
      messageLabel.textContent = text;
      lastMessageUntil = performance.now() + duration;
    }

    function canMoveTo(x, z, radius = .42) {
      if (Math.abs(x) > 43 || Math.abs(z) > 43) return false;
      return !obstacles.some(obstacle => Math.abs(x - obstacle.x) < obstacle.halfX + radius && Math.abs(z - obstacle.z) < obstacle.halfZ + radius);
    }

    function moveEntity(position, dx, dz) {
      if (canMoveTo(position.x + dx, position.z, .42)) position.x += dx;
      if (canMoveTo(position.x, position.z + dz, .42)) position.z += dz;
    }

    function hitEntity(entity, damage, attacker) {
      if (!entity.alive) return;
      if (entity === player && player.invulnerable > 0) return;
      entity.health -= damage;
      entity.lastHitBy = attacker;
      if (entity === player) {
        updateHud();
        showMessage('IMPACTO RECIBIDO', 550);
      }
      if (entity.health <= 0) {
        entity.health = 0;
        entity.alive = false;
        if (entity !== player) {
          scene.remove(entity.mesh);
          if (entity.lastHitBy === player) {
            player.kills += 1;
            showMessage('RIVAL ELIMINADO', 800);
          }
        } else {
          showMessage('HAS CAÍDO EN COMBATE', 2000);
        }
        updateHud();
        checkEnd();
      }
    }

    function checkEnd() {
      if (ended) return;
      const alive = livingCombatants().length + (player.alive ? 1 : 0);
      if (alive <= 1) {
        ended = true;
        running = false;
        statusLabel.textContent = 'COMBATE FINALIZADO';
        overlayCopy.textContent = player.alive
          ? `Has sobrevivido a los nueve rivales con ${player.kills} eliminación${player.kills === 1 ? '' : 'es'}. La arena ya tiene dueño.`
          : `Has conseguido ${player.kills} eliminación${player.kills === 1 ? '' : 'es'}. En la próxima partida, busca cobertura antes de disparar.`;
        startButton.innerHTML = 'VOLVER A JUGAR <span aria-hidden="true">↗</span>';
        overlay.classList.remove('hidden');
        crosshair.style.opacity = '0';
        if (document.pointerLockElement) document.exitPointerLock();
      }
    }

    function addTracer(from, to, color = '#d7fb61') {
      const geometry = new THREE.BufferGeometry().setFromPoints([from.clone(), to.clone()]);
      const material = new THREE.LineBasicMaterial({ color, transparent: true, opacity: .9 });
      const mesh = new THREE.Line(geometry, material);
      scene.add(mesh);
      tracers.push({ mesh, life: .075 });
    }

    function firePlayer() {
      const now = performance.now() / 1000;
      if (!player.alive || player.reloading || now - player.lastShot < .28) return;
      if (player.ammo <= 0) {
        showMessage('SIN MUNICIÓN · PULSA R', 700);
        player.lastShot = now;
        return;
      }
      player.lastShot = now;
      player.ammo -= 1;
      updateHud();
      raycaster.setFromCamera(center, camera);
      const targets = [];
      for (const bot of bots) if (bot.alive) targets.push(...bot.mesh.userData.parts);
      const coverHit = raycaster.intersectObjects(obstacleMeshes, false)[0];
      const hit = raycaster.intersectObjects(targets, false)[0];
      let end = raycaster.ray.origin.clone().addScaledVector(raycaster.ray.direction, 58);
      if (coverHit && (!hit || coverHit.distance < hit.distance)) end = coverHit.point;
      else if (hit) {
        const bot = bots.find(candidate => candidate.alive && candidate.mesh.userData.parts.includes(hit.object));
        if (bot) {
          end = hit.point;
          hitEntity(bot, 42, player);
          crosshair.classList.add('hit');
          setTimeout(() => crosshair.classList.remove('hit'), 100);
        }
      }
      const muzzle = camera.position.clone().addScaledVector(camera.getWorldDirection(new THREE.Vector3()), .65);
      addTracer(muzzle, end, '#d7fb61');
    }

    function reload() {
      if (!running || player.reloading || player.ammo === 12 || !player.alive) return;
      player.reloading = true;
      showMessage('RECARGANDO', 1000);
      updateHud();
      setTimeout(() => {
        if (!player.alive) return;
        player.ammo = 12;
        player.reloading = false;
        updateHud();
      }, 1050);
    }

    function hasLineOfSight(from, to) {
      const origin = from.clone();
      origin.y += 1.2;
      const target = to.clone();
      target.y += .9;
      const direction = target.sub(origin);
      const distance = direction.length();
      direction.normalize();
      raycaster.set(origin, direction);
      const obstruction = raycaster.intersectObjects(obstacleMeshes, false)[0];
      return !obstruction || obstruction.distance >= distance - .4;
    }

    function botShoot(bot, target, dt) {
      if (bot.shoot > 0 || !hasLineOfSight(bot.position, target.position)) return;
      bot.shoot = .85 + Math.random() * .65;
      const distance = bot.position.distanceTo(target.position);
      const hitChance = Math.max(.07, .48 - distance * .009);
      const start = bot.position.clone().add(new THREE.Vector3(0, 1.3, 0));
      const aim = target.position.clone().add(new THREE.Vector3(0, .82, 0));
      const miss = new THREE.Vector3((Math.random() - .5) * distance * .09, (Math.random() - .5) * distance * .055, (Math.random() - .5) * distance * .09);
      aim.add(miss);
      addTracer(start, aim, '#ff856c');
      if (Math.random() < hitChance) hitEntity(target, 9 + Math.random() * 5, bot);
    }

    function updateBots(dt) {
      const candidates = [...livingCombatants()];
      if (player.alive) candidates.push(player);
      for (const bot of bots) {
        if (!bot.alive) continue;
        bot.think -= dt;
        bot.shoot -= dt;
        if (bot.think <= 0 || !bot.target || !bot.target.alive) {
          bot.think = .3 + Math.random() * .25;
          let nearest = null;
          let nearestDistance = Infinity;
          for (const candidate of candidates) {
            if (candidate === bot || !candidate.alive) continue;
            const distance = bot.position.distanceTo(candidate.position);
            if (distance < nearestDistance) { nearest = candidate; nearestDistance = distance; }
          }
          bot.target = nearest;
          if (Math.random() < .25) bot.strafe *= -1;
        }
        const target = bot.target;
        if (!target) continue;
        const delta = new THREE.Vector3(target.position.x - bot.position.x, 0, target.position.z - bot.position.z);
        const distance = delta.length();
        if (distance > .001) {
          const angle = Math.atan2(delta.x, delta.z);
          bot.mesh.rotation.y = angle;
          let forward = distance > 13 ? 1 : distance < 7 ? -.45 : .12;
          let side = distance < 19 ? bot.strafe * .42 : 0;
          const dx = (Math.sin(angle) * forward + Math.cos(angle) * side) * bot.speed * dt;
          const dz = (Math.cos(angle) * forward - Math.sin(angle) * side) * bot.speed * dt;
          const oldX = bot.position.x;
          const oldZ = bot.position.z;
          moveEntity(bot.position, dx, dz);
          if (oldX === bot.position.x && oldZ === bot.position.z) bot.strafe *= -1;
          bot.mesh.position.copy(bot.position);
          if (distance < 27) botShoot(bot, target, dt);
        }
      }
    }

    function updatePlayer(dt) {
      player.invulnerable = Math.max(0, player.invulnerable - dt);
      const forwardInput = (held.w || held.arrowup ? 1 : 0) - (held.s || held.arrowdown ? 1 : 0);
      const sideInput = (held.d || held.arrowright ? 1 : 0) - (held.a || held.arrowleft ? 1 : 0);
      const length = Math.hypot(forwardInput, sideInput) || 1;
      const speed = held.shift ? 9.2 : 6.3;
      const forward = forwardInput / length * speed * dt;
      const side = sideInput / length * speed * dt;
      const dx = -Math.sin(player.yaw) * forward + Math.cos(player.yaw) * side;
      const dz = -Math.cos(player.yaw) * forward - Math.sin(player.yaw) * side;
      moveEntity(player.position, dx, dz);
      camera.position.set(player.position.x, 1.62, player.position.z);
      camera.rotation.set(player.pitch, player.yaw, 0, 'YXZ');
      if (held.fire) firePlayer();
    }

    function beginMatch() {
      resetMatch();
      running = true;
      overlay.classList.add('hidden');
      crosshair.style.opacity = '1';
      touchControls.classList.add('active');
      if (matchMedia('(pointer:fine)').matches) renderer.domElement.requestPointerLock?.();
    }

    startButton.addEventListener('click', beginMatch);
    document.addEventListener('pointerlockchange', () => {
      if (!document.pointerLockElement && running && matchMedia('(pointer:fine)').matches) {
        running = false;
        overlayCopy.textContent = 'Partida en pausa. Vuelve a la arena cuando estés listo.';
        startButton.innerHTML = 'CONTINUAR <span aria-hidden="true">↗</span>';
        overlay.classList.remove('hidden');
      } else if (document.pointerLockElement && !ended) {
        running = true;
        overlay.classList.add('hidden');
      }
    });
    document.addEventListener('mousemove', event => {
      if (document.pointerLockElement && running) {
        player.yaw -= event.movementX * .0022;
        player.pitch = THREE.MathUtils.clamp(player.pitch - event.movementY * .0022, -1.38, 1.38);
      }
    });
    renderer.domElement.addEventListener('pointerdown', event => {
      if (event.pointerType === 'touch' && running) {
        touchLookPointer = event.pointerId;
        touchLookX = event.clientX;
        touchLookY = event.clientY;
        renderer.domElement.setPointerCapture(event.pointerId);
      } else if (event.button === 0 && running && !document.pointerLockElement) {
        renderer.domElement.requestPointerLock?.();
      }
    });
    renderer.domElement.addEventListener('pointermove', event => {
      if (event.pointerType === 'touch' && event.pointerId === touchLookPointer && running) {
        player.yaw -= (event.clientX - touchLookX) * .006;
        player.pitch = THREE.MathUtils.clamp(player.pitch - (event.clientY - touchLookY) * .006, -1.25, 1.25);
        touchLookX = event.clientX;
        touchLookY = event.clientY;
      }
    });
    renderer.domElement.addEventListener('pointerup', event => { if (event.pointerId === touchLookPointer) touchLookPointer = null; });
    document.addEventListener('keydown', event => {
      const key = event.key.toLowerCase();
      held[key] = true;
      if (['arrowup','arrowdown','arrowleft','arrowright',' '].includes(key)) event.preventDefault();
      if (key === 'r') reload();
    });
    document.addEventListener('keyup', event => { held[event.key.toLowerCase()] = false; });
    document.addEventListener('mousedown', event => { if (event.button === 0 && running && document.pointerLockElement) held.fire = true; });
    document.addEventListener('mouseup', event => { if (event.button === 0) held.fire = false; });
    document.addEventListener('contextmenu', event => event.preventDefault());
    document.querySelectorAll('[data-key]').forEach(button => {
      const key = button.dataset.key;
      button.addEventListener('pointerdown', event => { event.preventDefault(); held[key] = true; button.setPointerCapture(event.pointerId); });
      const release = () => { held[key] = false; };
      button.addEventListener('pointerup', release);
      button.addEventListener('pointercancel', release);
      button.addEventListener('lostpointercapture', release);
    });
    const shootButton = document.querySelector('[data-shoot]');
    shootButton.addEventListener('pointerdown', event => { event.preventDefault(); held.fire = true; shootButton.setPointerCapture(event.pointerId); });
    for (const eventName of ['pointerup','pointercancel','lostpointercapture']) shootButton.addEventListener(eventName, () => { held.fire = false; });
    document.querySelector('[data-reload]').addEventListener('pointerdown', event => { event.preventDefault(); reload(); });

    function animate() {
      requestAnimationFrame(animate);
      const dt = Math.min(clock.getDelta(), .04);
      if (running && !ended) {
        updatePlayer(dt);
        updateBots(dt);
      }
      for (let i = tracers.length - 1; i >= 0; i--) {
        tracers[i].life -= dt;
        if (tracers[i].life <= 0) {
          scene.remove(tracers[i].mesh);
          tracers[i].mesh.geometry.dispose();
          tracers[i].mesh.material.dispose();
          tracers.splice(i, 1);  
        }
      }
      if (performance.now() > lastMessageUntil) messageLabel.textContent = '';
      renderer.render(scene, camera);
    }

    addEventListener('resize', () => {
      camera.aspect = innerWidth / innerHeight;
      camera.updateProjectionMatrix();
      renderer.setSize(innerWidth, innerHeight);
    });
    updateHud();
    animate();