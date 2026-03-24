/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Composer } from "@mail/core/common/composer";

patch(Composer.prototype, {

    // --------------------------
    // Template
    // --------------------------
    onClickTemplate() {
        const templateText = `
ชื่อลูกค้า:
เบอร์โทร:
จังหวัด:
รายละเอียด:
`;
        this._appendText(templateText);
    },

    // --------------------------
    // Source
    // --------------------------
    onChangeSource(ev) {
        const value = ev.target.value;
        if (!value) return;

        this._appendText(`\nลูกค้าจาก ${value}`);
        ev.target.value = "";
    },

    // --------------------------
    // Product
    // --------------------------
    onChangeProduct(ev) {
        const value = ev.target.value;
        if (!value) return;

        this._appendText(`\nสนใจสินค้า ${value}`);
        ev.target.value = "";
    },

    // --------------------------
    // 🔥 FINAL append (รองรับ Odoo 19)
    // --------------------------
    _appendText(text) {

        const composer = this.props?.composer;

        // ✅ วิธีที่ถูกที่สุด (ถ้ามี API)
        if (composer && composer.updateTextInputContent) {
            const current = composer.textInputContent || "";
            composer.updateTextInputContent(current + text);
            return;
        }

        // fallback (กันพัง)
        const root = this.root?.el;
        if (!root) return;

        const input = root.querySelector("textarea, div[contenteditable='true']");
        if (!input) return;

        if (input.tagName === "TEXTAREA") {
            input.value = (input.value || "") + text;
        } else {
            input.innerHTML += text.replace(/\n/g, "<br>");
        }

        input.dispatchEvent(new Event("input", { bubbles: true }));
    },

});