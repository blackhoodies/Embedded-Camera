const functions = require('firebase-functions');
const admin = require('firebase-admin');
admin.initializeApp(functions.config().firebase);

exports.sendNotification = functions.database.ref('/status/')
    .onUpdate(event => {
        var eventSnapshot = event.after;
        var statuss = eventSnapshot.child("status").val();
        if (statuss === "falling"){
            let messageObject = new Object();
            messageObject.notification = {
                title: "Đã phát hiện có người ngã",
                body: "Đề nghị truy cập vào ứng dụng để theo dõi tình hình và đưa ra hướng xử lý"
            };
            return admin.messaging().sendToTopic("broadcast", messageObject);
        }
        return 1;
    })
