/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Composer } from "@mail/core/common/composer";

patch(Composer.prototype, {

    // =========================================================
    // ✅ CHECK: ใช้เฉพาะ CRM (crm.lead)
    // =========================================================
    _isCRM() {
        return this.props?.composer?.thread?.model === "crm.lead";
    },

    // =========================================================
    // Template Button
    // =========================================================
    onClickTemplate() {
        if (!this._isCRM()) return;

        const templateText = `
ชื่อลูกค้า:
เบอร์โทร:
จังหวัด:
รายละเอียด:
`;

        this._appendText(templateText);
    },

    // =========================================================
    // Source Dropdown
    // =========================================================
    onChangeSource(ev) {
        if (!this._isCRM()) return;

        const value = ev.target.value;
        if (!value) return;

        this._appendText(`\nลูกค้าจาก ${value}`);
        ev.target.value = "";
    },

    // =========================================================
    // Product Dropdown
    // =========================================================
    onChangeProduct(ev) {
        if (!this._isCRM()) return;

        const value = ev.target.value;
        if (!value) return;

        this._appendText(`\nสนใจสินค้า ${value}`);
        ev.target.value = "";
    },

    // =========================================================
    // 🔥 Append Text (รองรับ Odoo 19 ทุก mode)
    // =========================================================
    _appendText(text) {
        const composer = this.props?.composer;

        // ✅ วิธีหลัก (OWL API)
        if (composer && composer.updateTextInputContent) {
            const current = composer.textInputContent || "";
            composer.updateTextInputContent(current + text);
            return;
        }

        // -----------------------------------------------------
        // ⚠️ Fallback (กันพังบาง instance)
        // -----------------------------------------------------
        const root = this.root?.el;
        if (!root) {
            console.warn("❌ [Mono] root not found");
            return;
        }

        const input = root.querySelector("textarea, div[contenteditable='true']");
        if (!input) {
            console.warn("❌ [Mono] input not found");
            return;
        }

        // textarea mode
        if (input.tagName === "TEXTAREA") {
            input.value = (input.value || "") + text;
        } 
        // rich editor mode
        else {
            input.innerHTML += text.replace(/\n/g, "<br>");
        }

        // trigger OWL update
        input.dispatchEvent(new Event("input", { bubbles: true }));
    },

    // =========================================================
    // 🔍 DEBUG (เปิดใช้ตอน debug ได้)
    // =========================================================
    /*
    mounted() {
        console.log("🔥 Composer Props:", this.props);
        console.log("🔥 Model:", this.props?.composer?.thread?.model);
    }
    */

});