/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { KanbanModel } from "@web/views/kanban/kanban_model";
import { ConfirmationDialog } from "@web/core/confirmation_dialog/confirmation_dialog";

patch(KanbanModel.prototype, {

    async moveRecord(recordId, targetGroupId, options = {}) {
        const confirmed = await new Promise((resolve) => {
            this.env.services.dialog.add(ConfirmationDialog, {
                title: "Confirm Status Change",
                body: "Are you sure you want to move this task?",
                confirm: () => resolve(true),
                cancel: () => resolve(false),
            });
        });

        if (!confirmed) {
            return;
        }

        return await super.moveRecord(recordId, targetGroupId, options);
    }

});