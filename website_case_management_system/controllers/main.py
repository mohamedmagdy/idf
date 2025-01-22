from odoo import http
from odoo.http import request
import base64

class WebsiteCaseManagement(http.Controller):

    @http.route(['/case'], type='http', auth='public', website=True)
    def case_submission_form(self, **kwargs):
        return request.render('website_case_management_system.case_submission_form')
    
    @http.route(['/case/form'], type='http', auth='public', website=True)
    def case_submission_form(self, **kwargs):
        return request.render('website_case_management_system.case_submission_form')

    @http.route(['/submit-case'], type='http', auth='public', website=True, methods=['POST'])
    def submit_case(self, **post):
        if not post:
            return request.redirect('/case/form')

        vals = {
            'contact_name': post.get('contact_name'),
            'contact_email': post.get('contact_email'),
            'contact_phone': post.get('contact_phone'),
            'contact_age': int(post.get('contact_age', 0)),
            'project_name': post.get('project_name'),
            'project_description': post.get('project_description'),
            'business_nature': post.get('business_nature'),
            'business_model': post.get('business_model'),
            'business_registration_type': post.get('business_registration_type'),
            'challenges': post.get('challenges'),
            'name': 'New',
            'company_registration_date': post.get('company_registration_date'),
            'competitive_advantage': post.get('competitive_advantage'),
            'sector_category': post.get('sector_category'),
            'problems_to_be_solved': post.get('problems_to_be_solved'),
            'business_start_date': post.get('business_start_date'),
            'funding_amount': float(post.get('funding_amount', 0.0)),
            'offered_services': post.get('offered_services'),
            'previous_investments': post.get('previous_investments'),
            'profit_model': post.get('profit_model'),
            'target_audience': post.get('target_audience'),
            'state': 'apply'
        }

        # Handle file uploads
        if 'business_plan' in request.httprequest.files:
            business_plan = request.httprequest.files['business_plan']
            vals['business_plan'] = base64.b64encode(business_plan.read())
            vals['is_business_plan'] = True

        if 'pitch_deck' in request.httprequest.files:
            pitch_deck = request.httprequest.files['pitch_deck']
            vals['pitch_deck'] = base64.b64encode(pitch_deck.read())
            vals['is_pitch_deck'] = True

        case = request.env['case.case'].sudo().create(vals)

        return request.render('website_case_management_system.case_submitted', {
            'case': case,
        }) 