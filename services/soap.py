import xml.etree.ElementTree as ET

import requests
from requests.auth import HTTPBasicAuth

from config import (
    SOAP_HOST,
    SOAP_PASSWORD,
    SOAP_PORT,
    SOAP_USERNAME,
)

SOAP_URL = f"http://{SOAP_HOST}:{SOAP_PORT}/"


def execute(command):
    xml = f"""<?xml version="1.0" encoding="utf-8"?>
<SOAP-ENV:Envelope
 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
 xmlns:xsd="http://www.w3.org/2001/XMLSchema"
 xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
  <SOAP-ENV:Body>
    <executeCommand xmlns="urn:AC">
      <command>{command}</command>
    </executeCommand>
  </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
"""

    response = requests.post(
        SOAP_URL,
        data=xml,
        headers={
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": "urn:AC#executeCommand",
        },
        auth=HTTPBasicAuth(
            SOAP_USERNAME,
            SOAP_PASSWORD,
        ),
        timeout=10,
    )

    root = ET.fromstring(response.text)

    namespaces = {
        "soap": "http://schemas.xmlsoap.org/soap/envelope/",
    }

    fault = root.find(".//soap:Fault", namespaces)
    if fault is not None:
        fault_string = fault.find("faultstring")
        if fault_string is not None and fault_string.text:
            return False, fault_string.text.strip()

    result = root.find(".//result")
    if result is not None and result.text:
        return True, result.text.strip()

    return False, "Unknown SOAP response."


def create_account(username, password):
    success, message = execute(f"account create {username} {password}")

    if success and message.startswith("Account created"):
        return (
            True,
            f"🎉 Your account has been created successfully!\n\n"
            f"**Username:** `{username}`\n\n"
            "You can now log into the server.",
        )

    if "already exist" in message.lower():
        return (
            False,
            "That username is already taken.\n\nPlease choose another username.",
        )

    return False, message


def change_password(username, password):
    success, message = execute(f"account set password {username} {password} {password}")

    if success or "password was changed" in message.lower():
        return (
            True,
            "Your password has been changed successfully.",
        )

    return False, message
