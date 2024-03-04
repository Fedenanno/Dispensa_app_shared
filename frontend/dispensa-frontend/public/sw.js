/**
 * Copyright 2018 Google Inc. All Rights Reserved.
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *     http://www.apache.org/licenses/LICENSE-2.0
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// If the loader is already loaded, just stop.
if (!self.define) {
    let registry = {};

    // Used for `eval` and `importScripts` where we can't get script URL by other means.
    // In both cases, it's safe to use a global var because those functions are synchronous.
    let nextDefineUri;

    const singleRequire = (uri, parentUri) => {
        uri = new URL(uri + ".js", parentUri).href;
        return registry[uri] || (

            new Promise(resolve => {
                if ("document" in self) {
                    const script = document.createElement("script");
                    script.src = uri;
                    script.onload = resolve;
                    document.head.appendChild(script);
                } else {
                    nextDefineUri = uri;
                    importScripts(uri);
                    resolve();
                }
            })

                .then(() => {
                    let promise = registry[uri];
                    if (!promise) {
                        throw new Error(`Module ${uri} didn’t register its module`);
                    }
                    return promise;
                })
        );
    };

    self.define = (depsNames, factory) => {
        const uri = nextDefineUri || ("document" in self ? document.currentScript.src : "") || location.href;
        if (registry[uri]) {
            // Module is already loading or loaded.
            return;
        }
        let exports = {};
        const require = depUri => singleRequire(depUri, uri);
        const specialDeps = {
            module: { uri },
            exports,
            require
        };
        registry[uri] = Promise.all(depsNames.map(
            depName => specialDeps[depName] || require(depName)
        )).then(deps => {
            factory(...deps);
            return exports;
        });
    };
}

define(['./workbox-6e3354dc'], (function (workbox) {
    'use strict';

    self.skipWaiting();
    workbox.clientsClaim();

    /**
     * The precacheAndRoute() method efficiently caches and responds to
     * requests for URLs in the manifest.
     * See https://goo.gl/S9QRab
     */
    workbox.precacheAndRoute([{
        "url": "registerSW.js",
        "revision": "3ca0b8505b4bec776b69afdba2768812"
    }, {
        "url": "index.html",
        "revision": "0.ud8prh05q7o"
    }], {});
    workbox.cleanupOutdatedCaches();
    workbox.registerRoute(new workbox.NavigationRoute(workbox.createHandlerBoundToURL("index.html"), {
        allowlist: [/^\/$/]
    }));

}));


//DEPRECATED
// //Se l'utente è registrato
// if (localStorage.getItem('id_user')) {
//     // Connessione al socket

//     const socket = new WebSocket(`ws://localhost:8000/ws/notifications/${localStorage.getItem('id_user')}`);
//     console.log('Connesso al socket - SW')
//     // Listener per la ricezione dei messaggi dal socket
//     socket.addEventListener('message', event => {
//         console.log('Messaggio ricevuto dal socket - SW');
//         const messageData = JSON.parse(event.data);
//         const notificationTitle = 'Nuovo Messaggio';
//         const notificationOptions = {
//             body: "Notifica dal service W"//messageData.body,

//         };
//         self.registration.showNotification(notificationTitle, notificationOptions);
//     });

//     // Gestione della richiesta di notifica push
//     self.addEventListener('push', event => {
//         const data = event.data.json();
//         const title = data.title;
//         const options = {
//             body: data.body,

//         };
//         event.waitUntil(self.registration.showNotification(title, options));
//     });


// }
// else {
//     console.log('Utente non registrato');
// }
