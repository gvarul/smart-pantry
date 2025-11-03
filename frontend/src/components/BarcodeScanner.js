import React, { useEffect, useRef } from "react";
import { Html5Qrcode } from "html5-qrcode";

export default function BarcodeScanner({ onDetected }) {
  const divId = "reader";
  const qrcodeRef = useRef(null);

  useEffect(() => {
    const html5QrCode = new Html5Qrcode(divId);
    qrcodeRef.current = html5QrCode;
    html5QrCode.start(
      { facingMode: "environment" },
      { fps: 10, qrbox: 250 },
      (decodedText, decodedResult) => {
        onDetected(decodedText);
        html5QrCode.stop().catch(err => console.error("stop failed", err));
      },
      (errorMessage) => {}
    ).catch(err => console.error("start failed", err));
    return () => {
      if (qrcodeRef.current) {
        qrcodeRef.current.stop().catch(() => {});
      }
    };
  }, [onDetected]);

  return <div id={divId} style={{ width: "300px", height: "300px" }} />;
}
